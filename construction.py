# def operation(S):
#     N = len(S)
#     result = [0] * N
#
#     def calc(T):
#         visited = [False] * N
#         countOfCompoments = 0
#
#         location = []
#         len_t = len(T)
#
#         for i in range(N - len_t + 1):
#             if S[i:i + len_t] == T:
#                 location.append(i)
#
#         parent = list(range(N))
#
#
#         def finding_x(x):
#             if parent[x] != x:
#                 parent[x] = finding_x(parent[x])
#             return parent[x]
#
#         def union(x, y):
#             rootX = finding_x(x)
#             rootY = finding_x(y)
#             if rootX != rootY:
#                 parent[rootX] = rootY
#
#
#         for pos in location:
#             for i in range(pos, pos + len_t - 1):
#                 union(i, i + 1)
#
#         for i in range(N):
#             if finding_x(i) == i:
#                 countOfCompoments += 1
#
#         return countOfCompoments
#
#     for length in range(1, N + 1):
#         for start in range(N - length + 1):
#             T = S[start:start + length]
#             comp_count = calc(T)
#             if comp_count <= N and (result[comp_count - 1] == 0 or result[comp_count - 1] > length):
#                 result[comp_count - 1] = length
#
#     return result
#
# S = input().strip()
# result = operation(S)
# print(" ".join(map(str, result)))


from collections import defaultdict

def operation(S):
    N = len(S)
    result = [0] * N
    substringLen = defaultdict(lambda: float('inf'))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    for length in range(1, N + 1):
        seen = set()
        for start in range(N - length + 1):
            T = S[start:start + length]
            if T in seen:
                continue
            seen.add(T)


            parent = list(range(N))
            positions = []
            len_t = len(T)

            for i in range(N - len_t + 1):
                if S[i:i + len_t] == T:
                    positions.append(i)

            for pos in positions:
                for i in range(pos, pos + len_t - 1):
                    union(i, i + 1)


            countCompo = len({find(i) for i in range(N)})


            if countCompo <= N:
                substringLen[countCompo] = min(substringLen[countCompo], length)

    for k in range(1, N + 1):
        result[k - 1] = substringLen[k] if substringLen[k] != float('inf') else 0

    return result

S = input().strip()
result = operation(S)
print(" ".join(map(str, result)))
