# Network-Dismentling-Problem（NDP）
network science -> network dismantling problem

The study of the network dismantling problem in complex networks focuses on identifying an optimal subset of nodes whose removal leads to:
(1) efficient fragmentation of the network, breaking it into small, disconnected components that no longer form a large-scale connected structure; and
(2) disruption of spreading processes at the minimal possible cost.
(3) the choice of the nodes to be included in the dismantling set was based on their degrees (favoring the inclusion of the most connected vertices) or some measure of their centrality.

# Similar combinatorial optimization problems
- Decycling problem: to find the smallest set of vertices whose removal makes the graph acylic,meaning it contains no cycles.
Given a graph G = (V, E), find the smallest set of nodes S \subseteq V such that removing S from the graph results in an acyclic graph.
	•	The resulting graph G[V \setminus S] must have no cycles.
	•	The set S is called a decycling set or a minimum feedback vertex set (FVS).
The decycling problem is to "break the loop structure of a graph", while the dismantling problem is to "break the connectivity structure of a graph". Both achieve structural transformation by deleting nodes, but they have different goals, results, and applicable fields. If the graph is a forest (i.e., acyclic), then removing at most 1/(C+1) of the nodes is sufficient to dismantle it into connected components of size no larger than C; therefore, decycling can serve as a preprocessing step for dismantling. In the limit, the two are equal.

## 🌟 Generalized network dismantling problem[(Janson S, Thomason A,2008)](https://doi.org/10.48550/arXiv.0709.1787).
# Definition
We can call S a C-dismantling set if its removal yields a graph with the largest component that has size at most C[(Janson S, Thomason A,2008)](
https://doi.org/10.48550/arXiv.0709.1787).

# Proof 
Determining whether the C-dismantling number of a graph is smaller than some constant is nondeterministic polynomial (NP)-complete decision problem.


## 🌟 Cost

Assumption1️⃣ that the cost of removing nodes is the same.
Assumption2️⃣ that the cost of removing nodes is different.

## Target
- Optimal destruction of “Large connected component（LCC）”

## 🌟 Properities
- Topology properities: node centrality
- Nontopology features:
- Spectral properties

## 🌟 what an optimal attack strategy is？
Random attack and target attack

## 🌟 Random network

🕸️ Scale-free NDP

🕸️ Erdos– R´enyi NDP

## 🌟 Real world network

# Future directio


🌟 Approximations
- Spin-glass theory & optimal percolation theory
- 
- [Node-Weighted Laplacian operator](https://www.pnas.org/doi/abs/10.1073/pnas.1806108116)  
