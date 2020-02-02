from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


def bellmanFord(graph,inintal,end):
    #CONVERT TO PROPER DS FOR ALGORITHM
    #number of vertices
    V=len(graph.weights)
    map_dict={}
    bel_graph=[]
    for idx,key in enumerate(graph.edges.keys()):
        map_dict[key]=idx
    src=map_dict[inintal]
    dst=map_dict[end]
    path=[]
    for edge in graph.weights:
        bel_graph.append([map_dict[edge[0]], map_dict[edge[1]], edge[(0, 1)]])

    # init all distances from source to all as INFINITE
    dist = [float("Inf")] * V
    dist[src] = 0
    # relax all edges |V|-1 times.
    for i in range(V- 1):
        # update dist value and parent index of adjacent values of picked vertex.
        # consider those which are still in queue.
        for u, v, w in bel_graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path.append()
    # check for negative weight cycles. If path obtained from above step (shortest distances)
    # is shorter, there's a cycle. So quit.
    for u, v, w in bel_graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Negative Cycles !")
            return
    #convert to normal graph

    # print distances
def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    total_weight=0
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    for idx in range(len(path)-1):
        total_weight+=graph.weights[(path[idx],path[idx+1])]
    return path,total_weight