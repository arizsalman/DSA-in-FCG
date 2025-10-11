'''Graph ek data structure hai jo objects (nodes/vertices) ke beech ke relationships (edges) ko represent karta hai.'''
'''Graphs har jagah use hote hain — jab bhi relationships ya connections represent karne ho.'''

'''🔹 Important point:

Graph connection-based structure hai, sequence-based nahi.

List [1, 4] aur [4, 1] dono same connection represent karte hain.

Matlab agar graph ka code ya edge order badal jaye, to print order alag ho sakta hai —
lekin connections same rehte hain.

Isiliye agar koi graph “dusre tarike se likhe” (jaise edges ka order badal de ya printing format badal de),
to structure same rehta hai, bas presentation different lagti hai'''


"""| Area                      | Use of 
| 🌍 **Maps & Navigation**   | Cities (nodes) aur roads (edges). GPS routes find karne me use hota hai (e.g., Google Maps).       |

| 💻 **Social Networks**    | Users = nodes, friendships/follows = edges. Facebook, Twitter, Instagram sab graphs pe based hain. |

| 🌐 **Internet/Web**       | Websites = nodes, hyperlinks = edges. Google ka PageRank algorithm isi par based hai.              |

| 🧠 **Machine Learning**   | Graph Neural Networks (GNNs) data relationships analyze karte hain.                                |

| 🖥️ **Computer Networks** | Routers aur connections graphs ke form me analyze kiye jate hain.                                  |

| 📊 **Data Organization**  | Relationships in databases (like Neo4j) are stored as graphs.                                      |

| 🧩 **Algorithms**         | Shortest path (Dijkstra), cycle detection, connected components, etc. — sab graph algorithms hain. |

"""


"""| Algorithm                      | Purpose  
| **BFS (Breadth-First Search)** | Graph ke nodes ko level-wise explore karta hai.                               |
| **DFS (Depth-First Search)**   | Graph ke nodes ko depth-wise explore karta hai.                               |
| **Dijkstra’s Algorithm**       | Shortest path find karta hai (like Google Maps).                              |
| **Kruskal / Prim’s Algorithm** | Minimum Spanning Tree (MST) banata hai.                                       |
| **Topological Sort**           | Directed Acyclic Graph (DAG) me order find karta hai (e.g., task scheduling). |
"""

"""🔹 Graph ka Representation (programming me kaise dikhate hain)

Adjacency Matrix

Ek 2D array jisme 1 dikhata hai ke connection hai aur 0 dikhata hai ke nahi."""


'''2. **Adjacency List**
- Har node ke saath uske connected nodes ki list hoti hai.'''
# n = 5
# edges = [(0, 1), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 0)]
# m = len(edges)
# print(n, m)


class Graph:
    def __init__(self, n_vertices, edges):
        self.data = [[]for _ in range(n_vertices)]
        for v1, v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)

    def __repr__(self):
        result = ""
        for i, j in enumerate(self. data):
            result += f" {i}:{j}\n"  # is me pura age ga += ke wajah se
            # result = f" {i}:{j}\n" # is me sirf ye ae ga  4:[1, 3, 0]  pur nahe .
            """to har iteration me result overwrite ho jaata —
               sirf last line bachi rehti.
               Isliye += use karte hain, taki har line append (add) hoti jaaye."""
        return result


graphs = Graph(5, [(0, 1), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 0)])

print(graphs)


# class GraphMatrix:
#     def __init__(self, n_vertices, edges):
# Intailize a matrix of all zeros
# self.data = [[0 for _ in range(n_vertices)]for _ in range(n_vertices)]
# """Loop chal ke 4 rows bana chuka hai ✅
#    Lekin print karte waqt Python ne sab ek hi line me dikha diya.❌(human-friendly nahi)
# """
#         print(self.data)
#         # fill edges in matrix
#         for i, j in edges:
#             self.data[i][j] = 1
#             self.data[j][i] = 1

#         for row in self.data:
#             print(row)


# edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
# g = GraphMatrix(4, edges)
class GraphList:
    def __init__(self, n_vertices, edges):
        self.data = [[0] for _ in range(n_vertices)]
        print(f'fs{self.data}')
        for u, v in edges:
            self.data[u].append(v)
            self.data[v].append(u)
            print(f'sf{self.data}')

    def bfs(graphs, source):
        visited = [False] * len(graphs.data)
        queue = [source]
        visited[source] = True
        i = 0
        while i < len(queue):
            current = queue[i]
            for v in graphs.data[current]:
                distance = 0
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True

            i += 1
        return queue


'''🔹 Tera sawal ka short answer:

matlab ke graphs = 4 or us 4 ke jo connection bane ke vo data ho ke?

✅ Bilkul haan (yes)
Lekin technically graphs ek object hai jisme:

4 vertices hain

aur unke connections graphs.data ke andar store hain'''
'''“Source node” = “Starting point” = “The first node from which BFS begins.”'''
edges = [(0, 1), (0, 2), (1, 3), (2, 4)]
graphs = GraphList(5, edges)

print(graphs.bfs(0))
