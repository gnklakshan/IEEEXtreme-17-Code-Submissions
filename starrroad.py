def dfs(city, last_stars, graph, stars, visited):
    visited[city] = True
    max_count = 0

    for neighbor in graph[city]:
        if not visited[neighbor]:
            # If the neighbor has more stars than the last restaurant dined
            if stars[neighbor] > last_stars:
                # Recursive DFS on the neighbor
                count = dfs(neighbor, stars[neighbor], graph, stars, visited)
                max_count = max(max_count, count + 1)  # Count this neighbor too

    visited[city] = False  # Backtrack
    return max_count


def max_dining_experience(N, stars, roads):
    # Create an adjacency list for the graph
    graph = [[] for _ in range(N)]
    for u, v in roads:
        graph[u - 1].append(v - 1)  # Adjust for 0-indexing
        graph[v - 1].append(u - 1)

    max_dine = 0

    # Try starting the journey from each city
    for i in range(N):
        visited = [False] * N
        # Start DFS from city i with its stars
        max_dine = max(max_dine, dfs(i, stars[i], graph, stars, visited))

    return max_dine


# Input reading
N = int(input())
stars = list(map(int, input().split()))
roads = [tuple(map(int, input().split())) for _ in range(N - 1)]

# Get the result
result = max_dining_experience(N, stars, roads)

# Output the result
print(result)
