# def two_fridges(substances):
#     n = len(substances)
#
#     if n == 0:
#         return 0, 0
#
#
#     fridge1_min, fridge1_max = -100, 100
#     fridge2_min, fridge2_max = -100, 100
#     for a, b in substances:
#         if b < fridge1_min or a > fridge1_max:
#             fridge2_min = max(fridge2_min, a)
#             fridge2_max = min(fridge2_max, b)
#         else:
#             fridge1_min = max(fridge1_min, a)
#             fridge1_max = min(fridge1_max, b)
#
#     # Final checks
#     if fridge1_min > fridge1_max or fridge2_min > fridge2_max or fridge1_max > fridge2_min:
#         return -1
#
#     return fridge1_min, fridge2_min
#
#
#
#
# N = int(input())
# substances = [tuple(map(int, input().split())) for _ in range(N)]
# print(two_fridges(substances))


def two_fridges(substances):
    n = len(substances)

    if n == 0:
        return -1  # According to the problem, return -1 if there are no substances.

    # Initialize ranges for fridge 1 and fridge 2.
    fridge1_min, fridge1_max = -100, 100
    fridge2_min, fridge2_max = -100, 100

    for a, b in substances:
        if b < fridge1_min or a > fridge1_max:
            # If substance cannot fit in fridge 1, try fridge 2
            fridge2_min = max(fridge2_min, a)
            fridge2_max = min(fridge2_max, b)
        else:
            # If substance can fit in fridge 1
            fridge1_min = max(fridge1_min, a)
            fridge1_max = min(fridge1_max, b)

    # Final checks
    if fridge1_min > fridge1_max or fridge2_min > fridge2_max or fridge1_max > fridge2_min:
        return -1

    # Ensure T1 <= T2
    T1 = fridge1_min
    T2 = fridge2_min if fridge1_max < fridge2_min else fridge1_max

    if T1 > T2 or T2 > 100 or T1 < -100:
        return -1

    return T1, T2

# Read input
N = int(input())
substances = [tuple(map(int, input().split())) for _ in range(N)]
result = two_fridges(substances)
print(result if result == -1 else f"{result[0]} {result[1]}")
