'''Graph ek data structure hai jo objects (nodes/vertices) ke beech ke relationships (edges) ko represent karta hai.'''
'''Graphs har jagah use hote hain — jab bhi relationships ya connections represent karne ho.'''

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
n = 5
edges = [(0, 1), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 0)]
m = len(edges)
print(n, m)


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
