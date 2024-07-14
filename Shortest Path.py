def get_graph():
    graph = {} # Initialize an empty dictionary to store the graph
    num_edges = int(input("Enter the number of edges: "))
    
    for _ in range(num_edges):
        node1 = input("Enter the start node: ") # Get the start node for the edge
        node2 = input("Enter the end node: ") # Get the end node for the edge
        weight = int(input(f"Enter the weight for the edge ({node1}-{node2}): ")) # Get the weight of the edge
        
        if node1 in graph:
            graph[node1].append((node2, weight)) # Add the edge to the start node's list if it exists
        else:
            graph[node1] = [(node2, weight)]  # Create a new list for the start node if it doesn't exist
        
        if node2 in graph:
            graph[node2].append((node1, weight)) # Add the edge to the end node's list if it exists
        else:
            graph[node2] = [(node1, weight)] # Create a new list for the end node if it doesn't exist
    
    return graph

def shortest_path(graph, start, target=''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        current = min(unvisited, key=distances.get) # Get the node with the smallest distance
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]: # Check if a shorter path is found
                distances[node] = distance + distances[current] # Update the shortest distance
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:] # Copy the current path if node is already in the path
                else:
                    paths[node] = paths[current][:] # Copy the current path
                paths[node].append(node) # Add the node to the path
        unvisited.remove(current) # Remove the current node from the unvisited list
    
    targets_to_print = [target] if target else graph # Determine which nodes to print
    for node in targets_to_print:
        if node == start:
            continue # Skip the start node
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths

def main():
    user_graph = get_graph()
    start_node = input("Enter the start node: ")
    target_node = input("Enter the target node (or press Enter to calculate distances to all nodes): ")
    shortest_path(user_graph, start_node, target_node)

main()
