dests = {
    'A': ['B', 'C', 'E'],
    'B': ['E', 'D'],
    'C': ['F'],
    'D': ['G'],
    'E': ['D', 'F', 'G'],
    'F': ['G'],
    'G': []
}



def find_ways(dests: dict) -> int:

    result = list(list(dests.keys())[0]) 
    result2 = []  

    while result:
        current_path = result.pop(0) 
        last_node = current_path[-1] 

        for neighbor in dests[last_node]:
            new_path = current_path + neighbor 
            if neighbor == 'G':              
                result2.append(new_path)
            else:
                result.append(new_path)      


    return len(result2)


print(find_ways(dests))
