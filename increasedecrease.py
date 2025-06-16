from itertools import permutations
from functools import lru_cache

def count_inversions(arr):
    if len(arr) < 2:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    merged, cross_inversions = merge_and_count(left, right)
    return merged, inv_left + inv_right + cross_inversions

def merge_and_count(left, right):
    merged = []
    i = j = 0
    inversions = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions

@lru_cache(None)
def target_permutation(N):
    mid = (N + 1) // 2
    target_first = sorted(range(1, mid + 1))
    target_last = sorted(range(mid + 1, N + 1), reverse=True)
    return target_first + target_last

def solve(N, M):
    total_swaps = 0
    for perm in permutations(range(1, N + 1)):
        target = target_permutation(N)
        target_indices = [target.index(p) for p in perm]
        _, swaps = count_inversions(target_indices)
        total_swaps = (total_swaps + swaps) % M
    return total_swaps

def main():
    N, M = map(int, input().split())
    result = solve(N, M)
    print(result)

if __name__ == "__main__":
    main()
