import cupy as cp
import h5py
import time
import sys
import os

n = int(sys.argv[1])

#uses slurm to get the gpu id
gpu_id = int(os.environ.get("SLURM_LOCALID", 0))
cp.cuda.Device(gpu_id).use()
print(f"Using GPU {gpu_id} for n={n}")

coords = cp.random.uniform(10000, 100000, (n, 2))
dist_matrix = cp.linalg.norm(coords[:, None, :] - coords[None, :, :], axis=2)

start_time = time.time()

paths = cp.zeros((1, 1), dtype=cp.int32)
distances = cp.zeros((1,), dtype=cp.float32)

for step in range(1, n):
    num_paths = paths.shape[0]
    expanded_paths = []
    expanded_distances = []

    visited_mask = cp.zeros((num_paths, n), dtype=bool)
    visited_mask[cp.arange(num_paths)[:, None], paths] = True

    for i in range(n):
        can_visit = ~visited_mask[:, i]
        if cp.any(can_visit):
            num_new = int(cp.sum(can_visit).item())
            fill_value = cp.array([i], dtype=cp.int32)
            new_paths = cp.concatenate(
                [paths[can_visit], cp.full((num_new, 1), fill_value, dtype=cp.int32)],
                axis=1
            )
            last_nodes = paths[can_visit][:, -1]
            new_distances = distances[can_visit] + dist_matrix[last_nodes, i]
            expanded_paths.append(new_paths)
            expanded_distances.append(new_distances)

    if expanded_paths:
        paths = cp.concatenate(expanded_paths, axis=0)
        distances = cp.concatenate(expanded_distances, axis=0)

last_nodes = paths[:, -1]
distances += dist_matrix[last_nodes, 0]

best_idx = cp.argmin(distances)
best_distance = distances[best_idx]
best_path = paths[best_idx]

elapsed_time = time.time() - start_time

print(f"Finished n={n}: Best distance = {best_distance:.2f}, Time = {elapsed_time:.4f} s")

filename = f"tsp_result_n{n}.h5"
with h5py.File(filename, "w") as f:
    grp = f.create_group(f"n_{n}")
    grp.create_dataset("path", data=cp.asnumpy(best_path))
    grp.create_dataset("distance", data=[float(best_distance)])
    grp.create_dataset("time_seconds", data=[elapsed_time])


#only runs on one gpu, need to eventually fix memory issues
