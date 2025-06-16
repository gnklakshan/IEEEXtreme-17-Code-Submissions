# # def minimum_stacks(N, x, bricks):
# #     bricks.sort()
# #
# #     stacks = []
# #
# #     for brick in bricks:
# #         placed = False
# #         for stack in stacks:
# #             if stack[-1] + x <= brick:
# #                 stack.append(brick)
# #                 placed = True
# #                 break
# #
# #         if not placed:
# #             stacks.append([brick])
# #
# #
# #     print(len(stacks))
# #     for stack in stacks:
# #         print(len(stack), ' '.join(map(str, reversed(stack))))
# #
# #
# # if __name__ == "__main__":
# #     N, x = map(int, input().split())
# #     bricks = list(map(int, input().split()))
# #
# #     minimum_stacks(N, x, bricks)
#
#
# def operation(num_bricks, offset, brick_l):
#     brick_l.sort()
#
#     stacks = []
#
#     for bri in brick_l:
#         placed = False
#         for stack in stacks:
#             if stack[-1] + offset <= bri:
#                 stack.append(bri)
#                 placed = True
#                 break
#
#         if not placed:
#             stacks.append([bri])
#
#     print(len(stacks))
#     for stack in stacks:
#         print(len(stack), ' '.join(map(str, reversed(stack))))
#
# if __name__ == "__main__":
#     num_bricks, offset = map(int, input().split())
#     brick_lengths = list(map(int, input().split()))
#
#     operation(num_bricks, offset, brick_lengths)


def operation( offset, brick_l):

    brick_l.sort()


    stacks = {}
    current_stack = 0

    for bri in brick_l:
        for stack_idx in range(current_stack + 1):
            if stack_idx not in stacks:
                stacks[stack_idx] = [bri]
                break
            if stacks[stack_idx][-1] + offset <= bri:
                stacks[stack_idx].append(bri)
                break
        else:
            stacks[current_stack + 1] = [bri]
            current_stack += 1

    print(len(stacks))
    for stack in stacks.values():
        print(len(stack), ' '.join(map(str, reversed(stack))))



num_bricks, offset = map(int, input().split())
brick_lengths = list(map(int, input().split()))
operation( offset, brick_lengths)