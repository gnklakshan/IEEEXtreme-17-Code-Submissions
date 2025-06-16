# import math
# from itertools import combinations
#
# def lcm(a, b):
#     return a * b // math.gcd(a, b)
#
# def count_hit_tiles(N, K, elasticities):
#     total_hits = 0
#
#
#     for i in range(1, K + 1):
#         for subset in combinations(elasticities, i):
#
#             current_lcm = subset[0]
#             for elasticity in subset[1:]:
#                 current_lcm = lcm(current_lcm, elasticity)
#
#                 if current_lcm > N:
#                     break
#             else:
#                 hits = N // current_lcm
#                 if i % 2 == 1:
#                     total_hits += hits
#                 else:
#                     total_hits -= hits
#
#     return total_hits
#
#
# import sys
# input = sys.stdin.read
# data = input().split()
# N = int(data[0])
# K = int(data[1])
# elasticities = list(map(int, data[2:2 + K]))
#
#
# result = count_hit_tiles(N, K, elasticities)
# print(result)


def count_hit_tiles(N, K, elasticities):
    hit_tiles = [False] * (N + 1)

    for elasticity in elasticities:
        for multiple in range(elasticity, N + 1, elasticity):
            hit_tiles[multiple] = True

    return sum(hit_tiles)


import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
K = int(data[1])
elasticities = list(map(int, data[2:2 + K]))

result = count_hit_tiles(N, K, elasticities)
print(result)
