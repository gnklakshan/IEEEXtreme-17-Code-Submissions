import math

def binomial(n, i):
    return math.comb(n, i)

def calc(k, n):
    result =[]
    range1 = pow(2,k)
    for t in range(range1 ):
        a = 0
        for i in range(n+1) :
            print(f'{t} --> {i}%{range1}')
            if (i % range1)==t:
                a += binomial(n,i)
        result.append(a)

    output = str(result[0] % 998244353)
    for items in result[1:]:
        output += ' ' + str(items % 998244353)

    print(output)


userinput = input()
k, n = map(int, userinput.split())
calc(k, n)

#
# def custom_sort(order, words):
#     order += order.upper()
#     order_map = {ch: idx for idx, ch in enumerate(order)}
#
#
#     # Custom key function for sorting
#     def sort_key(word):
#
#         return [order_map[ch] for ch in word]
#
#     # Sort the list of strings using the custom sort key
#     sorted_strings = sorted(words, key=sort_key)
#
#
#     return sorted_strings
#
#
# # Read input
# order = input().strip()
# N = int(input().strip())
# words = [input().strip() for _ in range(N)]
#
#
#
# sorted_strings = custom_sort(order, words)
#
# for string in sorted_strings:
#     print(string)
