from collections import deque

# ==========================================
# Example Graph: Represents a simple "city map"
# Each node = a city, edges = direct roads between them
# ==========================================
graph = {
    'Amman': ['Zarqa', 'Irbid'],   # Amman connected to Zarqa and Irbid
    'Zarqa': ['Amman', 'Mafraq'],  # Zarqa connected to Amman and Mafraq
    'Irbid': ['Amman', 'Ajloun'],  # Irbid connected to Amman and Ajloun
    'Mafraq': ['Zarqa'],           # Mafraq connected to Zarqa
    'Ajloun': ['Irbid']            # Ajloun connected to Irbid
}


# ==========================================
# Depth-First Search (DFS)
# ==========================================
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()   # Store visited nodes to avoid cycles

    visited.add(start)
    print(start, end=" ")

    # Explore neighbors recursively
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


# ==========================================
# Breadth-First Search (BFS)
# ==========================================
def bfs(graph, start):
    visited = set()
    queue = deque([start])   # Initialize queue with start node
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        # Explore neighbors level by level
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# ==========================================
# BFS Search for a specific city
# ==========================================
def search_bfs(graph, start, target):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        if node == target:
            return True   # Target found

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False   # Target not found


# ==========================================
# DFS Search for a specific city
# ==========================================
def search_dfs(graph, start, target, visited=None):
    if visited is None:
        visited = set()

    if start == target:
        return True

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            if search_dfs(graph, neighbor, target, visited):
                return True

    return False


# ==========================================
# Practical Tests
# ==========================================
print("DFS Traversal (Cities): ", end="")
dfs(graph, 'Amman')

print("\nBFS Traversal (Cities): ", end="")
bfs(graph, 'Amman')

# Search examples
print("\n\nSearch BFS for 'Ajloun':", search_bfs(graph, 'Amman', 'Ajloun'))   # True
print("Search BFS for 'Aqaba':", search_bfs(graph, 'Amman', 'Aqaba'))         # False

print("Search DFS for 'Mafraq':", search_dfs(graph, 'Amman', 'Mafraq'))       # True
print("Search DFS for 'Jerash':", search_dfs(graph, 'Amman', 'Jerash'))       # False)
