def calculate_optimal_cost(A):
    N = len(A)
    optimal_costs = []

    for l in range(N):
        for r in range(l, N):
            # Calculate the optimal cost for the subarray A[l...r]
            length = r - l + 1
            if length % 2 == 0:
                # If even, group elements into pairs
                max_sum = float('-inf')
                for i in range(length // 2):
                    max_sum = max(max_sum, A[l + i] + A[r - i])
            else:
                # If odd, one group will have a single element
                max_sum = float('-inf')
                for i in range(length // 2):
                    max_sum = max(max_sum, A[l + i] + A[r - i])
                max_sum = max(max_sum, A[l + length // 2])  # single element case

            optimal_costs.append(max_sum)

    return optimal_costs


def process_queries(N, A, Q, queries):
    # Precompute optimal costs for all subarrays
    optimal_costs = calculate_optimal_cost(A)

    # Now we need to handle the queries
    results = []

    for x in queries:
        total_sum = 0
        # Check each subarray
        for l in range(N):
            for r in range(l, N):
                cost_index = (r - l) * (r - l + 1) // 2 + l
                if optimal_costs[cost_index] <= x:
                    total_sum += (A[r] - A[l])
        results.append(total_sum)

    return results


# Input reading
N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [int(input().strip()) for _ in range(Q)]

# Process the queries
results = process_queries(N, A, Q, queries)

# Print results
for result in results:
    print(result)
