from collections import deque
graph = {
    "Alice": ["Charlie", "David"],
    "Charlie": ["Alice", "Emma"],
    "David": ["Alice", "Emma", "Fred"],
    "Emma": ["Bob", "Charlie", "David"],
    "Fred": ["Bob", "David"],
    "Bob": ["Emma", "Fred"]
    }
for node in graph:
    graph[node].sort()
    def bfs(graph, start, goal):
        queue = deque([[start]])
        visited = []
        print("\n========== BFS Traversal ==========")
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node not in visited:
                visited.append(node)
                print(f"\nCurrent Node : {node}")
                print("Queue :", list(queue))
                print("Visited :", visited)
                if node == goal:
                    print("\nGoal Found!")
                    return path
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        new_path = list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)
                        return None
                    def dfs(graph, start, goal):
                        stack = [[start]]
                        visited = []
                        print("\n========== DFS Traversal ==========")
                        while stack:
                            path = stack.pop()
                            node = path[-1]
                            if node not in visited:
                                visited.append(node)
                                print(f"\nCurrent Node : {node}")
                                print("Stack :", stack)
                                print("Visited :", visited)
                                if node == goal:
                                    print("\nGoal Found!")
                                    return path
                                for neighbour in reversed(graph[node]):
                                    if neighbour not in visited:
                                        new_path = list(path)
                                        new_path.append(neighbour)
                                        stack.append(new_path)
                                        return None
                                    source = "Alice"
                                    goal = "Bob"
                                    print("Source :", source)
                                    print("Goal   :", goal)
                                    bfs_path = bfs(graph, source, goal)
                                    print("\nBFS Shortest Path")
                                    print(" -> ".join(bfs_path))
                                    dfs_path = dfs(graph, source, goal)
                                    print("\nDFS Path")
                                    print(" -> ".join(dfs_path))