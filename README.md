# TSP_CUDA
This project is my final project for Special Topics - HPC Fall 25 at The University of Montana, this project utilized The University of Montana Research Cluster Hellgate.

# Background
The Traveling Salemsan Problem is a NP-hard computational problem formulated by William Rowan Hamilton and Thomas Kirkman in the 19th Century <sup>[<a href="#ref1">1</a>]</sup>. The core of this problem is to compute the weighted distance between a starting node in a graph, then traveling to all other nodes and returning to the starting node.

The Traveling Salesman Problem is an NP-Hard problem, meaning it cannot be run in Polynomial time, its computation alone would be $$\frac{(n-1)!}{2}$$ per graph <sup>[<a href="#ref2">2</a>]</sup>. This is because the problem starts at a selected node, computes all paths to other nodes and back, and then finds the lease weighted path.

$$
\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}
$$

# Installation

# Running the Scripts

# References
<a id="ref1"></a>[1] Wikipedia Contributors, “Travelling salesman problem,” Wikipedia, Jul. 14, 2019. https://en.wikipedia.org/wiki/Travelling_salesman_problem
<a id="ref2"></a>[2] https://d1wqtxts1xzle7.cloudfront.net/32636910/Traveling_Salesman_Problem__Theory_and_Applications_%281%29.pdf20131227-21724-81s0ew-libre-libre.pdf?1388153417=&response-content-disposition=inline%3B+filename%3DEstimativa_de_consumo_de_sodio_pela_popu.pdf&Expires=1763663180&Signature=YQ2QFlmDyrcsT5jG3O9ux1oKYoHOXPrDyOXQ4f~9CzR2namZNUHQeOeDZBTPKrCEEusiX0Q51QvKwI~qQ3RpcNU2-IMkiDkz~UYTSQ8KJ-ZdQoYoRO7EOEQO9iNMT~X6ZANbB54E78EFJAAQVyMXHw8vrR45rcmw5RulkjxI2nvHqc2AAk82SZUu5bU3Ue3kLNBzXFXPVoMx-EPb1zNfEya3YRrrzoUf1XToJxWnegOCMJ1S-5nw6JRABy6pAGTW-R-gZLAGT~uhPktUeaIfZCo9HM4HAKs020N9iZRiLnOSHQ1pPIPU5lJkrJ8MesuAUljQLi2eJvEg0yxJ0qGAHg__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA#page=13
