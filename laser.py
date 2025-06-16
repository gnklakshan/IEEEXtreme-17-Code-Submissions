
# def cal(L, N, M, beams_A, beams_B):
#     areas = N+1
#     vertical_beams = set()
#     horizontal_beams = set()
#     for d, coordinates in beams_A:
#         if d == 'R':
#             vertical_beams.add(coordinates)
#         elif d == 'U':
#             horizontal_beams.add(coordinates)
#
#
#     for d, coordinates in beams_B:
#         if (d=='L'):
#             areas += N+1
#         else:
#             if d == 'U':
#                 temp =0
#                 for i in horizontal_beams:
#                     if i == coordinates or i < coordinates:
#
#                         temp += 1
#                 # print("areas add",(len(horizontal_beams)-temp)+1+len(vertical_beams))
#                 areas += (len(horizontal_beams)-temp)+1+len(vertical_beams)
#
#
#     return areas
#
# # Input reading
# L, N, M = map(int, input().split())
#
# beams_A = []
# for _ in range(N):
#     d, c = input().split()
#     beams_A.append((d, int(c)))
#
# beams_B = []
# for _ in range(M):
#     d, c = input().split()
#     beams_B.append((d, int(c)))
#
# # Calculate and output the result
# print(cal(L, N, M, beams_A, beams_B))




def cal(L, N, M, beams_A, beams_B):
    areas = N + 1
    vertical_beams = set()
    horizontal_beams = set()

    for d, coordinates in beams_A:
        if d == 'R':
            vertical_beams.add(coordinates)
        elif d == 'U':
            horizontal_beams.add(coordinates)

    horizontal_beams = sorted(horizontal_beams)

    for d, coordinates in beams_B:
        if d == 'L':
            areas += N + 1
        elif d == 'U':
            temp = 0
            for i in horizontal_beams:
                if i > coordinates:
                    break
                temp += 1
            areas += (len(horizontal_beams) - temp) + 1 + len(vertical_beams)

    return areas


# Input reading
L, N, M = map(int, input().split())

beams_A = [tuple(input().split()) for _ in range(N)]
beams_A = [(d, int(c)) for d, c in beams_A]

beams_B = [tuple(input().split()) for _ in range(M)]
beams_B = [(d, int(c)) for d, c in beams_B]

# Calculate and output the result
print(cal(L, N, M, beams_A, beams_B))