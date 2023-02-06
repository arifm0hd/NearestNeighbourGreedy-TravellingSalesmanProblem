#  Nearest Neighbour Greedy - TSP | CSCI3302 GROUP PROJECT

This is a project for the Data Structures and Algorithm course, CSCI3302. This project is supposedly purposed to solve a specific instance of the Traveling Salesman Problem called the eil51. The eil51 TSP (Traveling Salesman Problem) is a well-known optimization problem in the field of operations research. It refers to the problem of finding the shortest route that visits a set of 51 cities (depots) and returns to the starting city, such that each city is visited exactly once. The eil51 TSP is often used as a benchmark for evaluating the performance of TSP solvers, as the problem size is small enough to obtain optimal solutions in reasonable time, yet challenging enough to test the quality of the solutions.

As a group we did a study on the performance of the **Greedy VS Dynamic Programming and its modifications in solving the Traveling Salesman Problem**.

I was responsible on working on the **Greedy Approach** combined with the **Nearest Neighbor Algorithm (NND) from Both
End-Points**

## How-to-Use
Not much just run the code really. The input has been predefined for the eil51 instance of the TSP.

## Results (Total Path Distance)
| Greedy    | NND + Greedy     |
| :-------- | :-------         |
| `479.43`  | `544.41`         |

## Findings
- Theory wise the NND + Greedy would have better performance compared to Greedy only approach. However, results showed that the performance favors Greedy over NND + Greedy.
- The factor to such outcome most probably be the implementation of the algorithms.


## Group Members

- Mohamad Akmal Arif Bin Mohamad Kamal Arifin **[2017151]**
- [Muhd Afiq Husyairi Bin Mohd Fadzli **[2018769]**](https://github.com/Kuasawan-Murbawan/Improved-Greedy-Crossover)
- Muhammad Aiman bin Mat Isa **[2014243]**
- Muhammad Afiq bin Kharul Azman **[2011595]**

## References

- Kizilateş, G., &amp; Nuriyeva, F. (2013). On the nearest neighbor algorithms for the traveling salesman problem. Advances in Intelligent Systems and Computing, 111–118. https://doi.org/10.1007/978-3-319-00951-3_11 

- jkinable. EIL51 Dataset · Jorlib/eil51.tsp. GitHub. Retrieved January 13, 2023, from https://github.com/coin-or/jorlib/blob/master/jorlib-core/src/test/resources/tspLib/tsp/eil51.tsp

- Liam Fell, &amp; mateuszlomateuszlo. Understanding EUC_2D Edge Weighting. Stack Overflow. Retrieved January 13, 2023, from https://stackoverflow.com/questions/46026163/understanding-euc-2d-edge-weighting 
