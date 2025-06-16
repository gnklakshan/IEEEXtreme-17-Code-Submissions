def maximize_number(N, K):
    num_str = list(str(N))
    length = len(num_str)

    def find_max(num_list, swaps, current_index):
        if swaps == 0 or current_index == length:
            return int(''.join(num_list))

        max_num = int(''.join(num_list))
        for i in range(current_index, length):
            for j in range(i + 1, length):
                if num_list[i] < num_list[j]:
                    num_list[i], num_list[j] = num_list[j], num_list[i]
                    max_num = max(max_num, find_max(num_list, swaps - 1, current_index + 1))
                    num_list[i], num_list[j] = num_list[j], num_list[i]

        return max_num

    return find_max(num_str, K, 0)


# Read input
N, K = map(int, input().split())
result = maximize_number(N, K)
print(result)
