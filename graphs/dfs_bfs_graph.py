from collections import deque

# Simple graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}


# Depth-First Search (DFS) implementation
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(f"DFS: Visited Room {start}, Visited Now {visited}")

    for neighbor in graph[start]:
        if neighbor not in visited:
            print(f"Moving to room {neighbor}")
            dfs(graph, neighbor, visited)

    return visited


# Breadth-First Search (BFS) implementation
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(f"Visited room {node}, Visited Now {visited}, Queue Now {list(queue)}")

        for neighbor in graph[node]:  # Corrected to use current node
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"BFS Added room {neighbor} to the queue.")


# -------------------- Example Usage --------------------
if __name__ == "__main__":
    print("=== DFS Practical ===")
    dfs(graph, 'A')

    print("\n=== BFS Practical ===")
    bfs(graph, 'A')
