# from typing import List, Tuple
# import math
#
#
# def get_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
#     """Calculate Euclidean distance between two points."""
#     return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
#
#
# def get_triumvirate_stability(points: List[Tuple[int, int]], i: int, j: int, k: int) -> float:
#     """Calculate stability of a triumvirate (max distance - min distance)."""
#     d1 = get_distance(points[i], points[j])
#     d2 = get_distance(points[j], points[k])
#     d3 = get_distance(points[i], points[k])
#     return max(d1, d2, d3) - min(d1, d2, d3)
#
#
# def find_best_triumvirate(N: int, points: List[Tuple[int, int]], used: List[bool]) -> List[int]:
#     """Find the next best triumvirate with minimum stability."""
#     min_stability = float('inf')
#     best_group = None
#
#     # Find first unused point
#     start = -1
#     for i in range(N):
#         if not used[i]:
#             start = i
#             break
#
#     if start == -1:
#         return None
#
#     # Try all possible combinations with this start point
#     for j in range(start + 1, N):
#         if used[j]:
#             continue
#         for k in range(j + 1, N):
#             if used[k]:
#                 continue
#
#             stability = get_triumvirate_stability(points, start, j, k)
#             if stability < min_stability:
#                 min_stability = stability
#                 best_group = [start, j, k]
#
#     return best_group
#
#
# def solve(N: int, points: List[Tuple[int, int]]) -> List[List[int]]:
#     """Main solver function."""
#     result = []
#     used = [False] * N
#
#     # Find N/3 triumvirates
#     for _ in range(N // 3):
#         group = find_best_triumvirate(N, points, used)
#         if group is None:
#             break
#
#         # Mark points as used
#         for idx in group:
#             used[idx] = True
#
#         result.append(group)
#
#     return result
#
#
# def main():
#     # Read input
#     N = int(input())
#     points = []
#     for _ in range(N):
#         x, y = map(int, input().split())
#         points.append((x, y))
#
#     # Get solution
#     triumvirates = solve(N, points)
#
#     # Print output
#     for group in triumvirates:
#         print(" ".join(map(str, group)))
#
#
# if __name__ == "__main__":
#     main()


import math
# def is_power_of_3(N):
#     if N == 0:
#         return "-1"
#     if N == 1:
#         return "0"
#
#     power = 0
#
#     while N > 1:
#         if N % 3 != 0:
#             return "-1"
#         N //= 3
#         power += 1
#
#     return str(power)

import math


def log_base_3(N):
    if N <= 0:
        return -1

    log_val = round(math.log(N, 3), 6)

    if 3 ** round(log_val) == N:
        return int(round(log_val))
    else:
        return -1


n = int(input().strip())
result = log_base_3(n)
print(result)
