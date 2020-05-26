**Network flow algorithms**

As many problems can be represented as a network of vertices and edges with capacity associated with each edge, there are list of algorithms that solve these problems like maximum flow. I took my time to study this problem and I am gonna share with you here my experience and the implementation of solving the issue with some of my edits.

**Resources and what to learn**

 1. !IMPORTANT understanding the max flow min cut theorem. Maybe this is the most important video to watch: [13. Incremental Improvement: Max Flow, Min Cut](https://www.youtube.com/watch?v=VYZGlgzr_As). Here he explains many of flow network properties so it is crucial to understand them as when you read about residual graph and augmenting path it will be easy.
 2. Sometimes less academic explanation with beautiful animation can help us: [Max Flow Ford Fulkerson | Network Flow | Graph Theory](https://www.youtube.com/watch?v=LdOnanfc5TM) and [Edmonds Karp Algorithm | Network Flow | Graph Theory](https://www.youtube.com/watch?v=RppuJYwlcI8)
 3. Wikipedia has great explanation: [Maximum flow problem](https://en.wikipedia.org/wiki/Maximum_flow_problem) and [Ford–Fulkerson algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm)

My implementation is based on the one in [Ford–Fulkerson algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm). I added some prints to watch the steps of the algorithm. It uses BFS to search for augmenting path (Edmonds–Karp algorithm).

**Simple Definitions**

 - Augmenting ***path***: it is list of edges that connect source (s) -> sink (t) and at the same time they have available capacity to deliver flow. 
 - Max flow of a path is the min capacity of one of the edges in the path. Example: I have 3 edges with following capacities (s) -> (6) -> (2) -> (8) -> (t). Imagine it like: from the source I can't deliver more than 2 through this path. It is a bottlenck. 

**Algorithm simply explained**
 - First step is to transform from original graph where every edge has a capacity to redsidual graph with forward edge and backward edge.
 - Through these edges we will keep applying BFS again and again from source (s) to sink (t) just to find the shortest path. This path is the agumenting apth. As long as there is a path to sink: I can send flow through it which means I still do not know what the maxflow is 😁.
 - When there is no enough capacity to send flow from source to sink.\
 - Remember since I looped through the paths before I will get the max flow of each path: sum it to global variable and final result will be the max flow of the network 🙂.