# def find_doubled_sequence(N):
#
#
#     if N  == 1:  # No valid sequence for even N
#         return [1,1]
#
#     sequence = [0] * (2 * N)
#     for i in range(1, N + 1):
#         left_index = i - 1
#         right_index = i - 1 + i + 1
#         if right_index >= 2 * N or sequence[left_index] != 0 or sequence[right_index] != 0:
#             return -1
#         sequence[left_index] = i
#         sequence[right_index] = i
#
#     return sequence


def find_doubled_sequence(N):
    if N == 1:  # No valid sequence for even N
        return [1, 1]

    sequence = [0] * (2 * N)
    for i in range(1, N + 1):
        left_index = i - 1
        right_index = i - 1 + i + 1
        if right_index >= 2 * N or sequence[left_index] != 0 or sequence[right_index] != 0:
            return -1
        sequence[left_index] = i
        sequence[right_index] = i

    return sequence

def process_test_cases(test_cases):
    results = []
    for N in test_cases:
        result = find_doubled_sequence(N)
        if result == -1:
            results.append("-1")
        else:
            results.append(" ".join(map(str, result)))

    print(results)
    return results

# Input processing
T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]

# Process test cases
results = process_test_cases(test_cases)

# Output results
for result in results:
    print(result)
