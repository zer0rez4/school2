dests = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'E', 'D'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['A', 'B', 'F', 'G'],
    'F': ['C', 'E', 'G'],
    'G': ['D', 'E', 'F']
}

def count_ways(graph, start, end, visited=None):
    
    if visited is None:
        visited = set()
    
    if start == end:
        return 1
    
    visited.add(start)
    
    total_paths = 0
    for neighbor in graph[start]:
        if neighbor not in visited:
            total_paths += count_ways(graph, neighbor, end, visited)
    
    visited.remove(start)
    return total_paths



result = count_ways(dests, 'A', 'G')

print(result)
