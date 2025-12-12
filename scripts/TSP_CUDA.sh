#!/bin/bash
#SBATCH --job-name=TSP-Array-GPU
#SBATCH --output=/mnt/beegfs/scratch/na193353/TSP_CUDA/tsp_array_%A_%a.out
#SBATCH --error=/mnt/beegfs/scratch/na193353/TSP_CUDA/tsp_array_%A_%a.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gpus-per-task=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=7-00:00:00
#SBATCH --partition=gpu(all)
#SBATCH --array=1-40

IMAGE=/mnt/beegfs/scratch/na193353/TSP_CUDA/tsp_gpu.sif

OUTDIR=/mnt/beegfs/scratch/na193353/TSP_CUDA

mkdir -p $OUTDIR

echo "Running on node: $(hostname)"
nvidia-smi

# Run inside container
apptainer exec --nv \
    --bind $OUTDIR:/output \
    --bind $PWD:/workspace \
    $IMAGE \
    python3 /workspace/TSP_CUDA.py $SLURM_ARRAY_TASK_ID /output


