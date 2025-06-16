MOD = 998244353


def count_permutations(N, C, R, B):
    possible_values = set(range(1, 2 * N + 1))
    used = set(c for c in C if c != -1)
    unused = list(possible_values - used)

    count = 1

    for i in range(N):
        a1, a2 = C[2 * i], C[2 * i + 1]
        b = B[i]
        r = R[i]

        # Process known values
        if a1 != -1 and a2 != -1:
            if (r == 0 and min(a1, a2) != b) or (r == 1 and max(a1, a2) != b):
                return 0
        elif a1 != -1:
            if (r == 0 and a1 >= b) or (r == 1 and a1 <= b):
                return 0
        elif a2 != -1:
            if (r == 0 and a2 >= b) or (r == 1 and a2 <= b):
                return 0
        else:
            # Both a1 and a2 are -1 (unknown)
            remaining_values = len(unused)
            valid_count = 0

            if r == 0:
                # Need values < b
                valid_count = len([x for x in unused if x < b])
            else:
                # Need values > b
                valid_count = len([x for x in unused if x > b])

            # We can choose 2 values from valid_count in any order
            if valid_count < 2:
                return 0

            count *= (valid_count * (valid_count - 1) // 2) % MOD
            count %= MOD

            # Update the unused values by removing the chosen pair
            unused = [x for x in unused if x not in [b for b in (valid_count, valid_count - 1)]]

    return count


# Reading inputs
N = int(input())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
B = list(map(int, input().split()))

# Get the answer
result = count_permutations(N, C, R, B)
print(result)
