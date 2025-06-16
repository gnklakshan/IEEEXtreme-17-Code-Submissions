# def alice_wins_probability(R1, B1, R2, B2):
#     # Initialize a 4D DP table with None (indicating uncomputed states)
#     dp = [[[[None for _ in range(41)] for _ in range(41)] for _ in range(41)] for _ in range(41)]
#
#     def calculate_probability(r1, b1, r2, b2, turn):
#         # Base cases
#         if r1 == 0 or b1 == 0:  # Alice runs out of stones
#             return 0.0
#         if r2 == 0 or b2 == 0:  # Bob runs out of stones
#             return 1.0
#         if dp[r1][b1][r2][b2] is not None:
#             return dp[r1][b1][r2][b2]
#
#         # Compute probabilities based on turn
#         if turn == 0:  # Alice's turn (A)
#             # Alice chooses red or blue; maximize her winning probability
#             win_prob_red = (r2 / (r2 + b2)) * calculate_probability(r1, b1, r2 - 1, b2, 1) + \
#                            (b2 / (r2 + b2)) * calculate_probability(r1 - 1, b1, r2, b2, 1)
#             win_prob_blue = (r2 / (r2 + b2)) * calculate_probability(r1, b1, r2, b2 - 1, 1) + \
#                             (b2 / (r2 + b2)) * calculate_probability(r1, b1 - 1, r2, b2, 1)
#             result = max(win_prob_red, win_prob_blue)
#         else:  # Bob's turn (B)
#             # Bob chooses red or blue; minimize Alice's winning probability
#             win_prob_red = (r1 / (r1 + b1)) * calculate_probability(r1 - 1, b1, r2, b2, 0) + \
#                            (b1 / (r1 + b1)) * calculate_probability(r1, b1 - 1, r2, b2, 0)
#             win_prob_blue = (r1 / (r1 + b1)) * calculate_probability(r1, b1, r2 - 1, b2, 0) + \
#                             (b1 / (r1 + b1)) * calculate_probability(r1, b1, r2, b2 - 1, 0)
#             result = min(win_prob_red, win_prob_blue)
#
#         dp[r1][b1][r2][b2] = result
#         return result
#
#     # Start with Alice's turn (0)
#     return calculate_probability(R1, B1, R2, B2, 0)
#
# # Read inputs
# R1, B1, R2, B2 = map(int, input().split())
# print(f"{alice_wins_probability(R1, B1, R2, B2):.6f}")


def calculate_probability(r1, b1, r2, b2, turn, memo):
    # Base cases
    if r1 == 0 or b1 == 0:  # Alice loses
        return 0.0
    if r2 == 0 or b2 == 0:  # Bob loses
        return 1.0

    # Check if the result is already computed
    if (r1, b1, r2, b2, turn) in memo:
        return memo[(r1, b1, r2, b2, turn)]

    if turn == 0:  # Alice's turn (maximize her probability)
        total_stones_bob = r2 + b2

        # Alice chooses red
        prob_if_red = (r2 / total_stones_bob) * calculate_probability(r1 - 1, b1, r2, b2, 1, memo)  # Bob guesses right
        prob_if_red += (b2 / total_stones_bob) * calculate_probability(r1, b1, r2 - 1, b2, 1, memo)  # Bob guesses wrong

        # Alice chooses blue
        prob_if_blue = (r2 / total_stones_bob) * calculate_probability(r1, b1 - 1, r2, b2, 1, memo)  # Bob guesses right
        prob_if_blue += (b2 / total_stones_bob) * calculate_probability(r1, b1, r2, b2 - 1, 1,
                                                                        memo)  # Bob guesses wrong

        # Maximum probability Alice can achieve
        result = max(prob_if_red, prob_if_blue)

    else:  # Bob's turn (minimize Alice's probability)
        total_stones_alice = r1 + b1

        # Bob chooses red
        prob_if_red = (r1 / total_stones_alice) * calculate_probability(r1, b1, r2 - 1, b2, 0,
                                                                        memo)  # Alice guesses right
        prob_if_red += (b1 / total_stones_alice) * calculate_probability(r1 - 1, b1, r2, b2, 0,
                                                                         memo)  # Alice guesses wrong

        # Bob chooses blue
        prob_if_blue = (r1 / total_stones_alice) * calculate_probability(r1, b1, r2, b2 - 1, 0,
                                                                         memo)  # Alice guesses right
        prob_if_blue += (b1 / total_stones_alice) * calculate_probability(r1 - 1, b1, r2, b2, 0,
                                                                          memo)  # Alice guesses wrong

        # Minimum probability Bob can force Alice to achieve
        result = min(prob_if_red, prob_if_blue)

    # Store the result in memo
    memo[(r1, b1, r2, b2, turn)] = result
    return result


def alice_winning_probability(R1, B1, R2, B2):
    memo = {}
    return calculate_probability(R1, B1, R2, B2, 0, memo)


# Example inputs
R1, B1, R2, B2 = 1, 2, 3, 4
probability = alice_winning_probability(R1, B1, R2, B2)
print(f"{probability:.9f}")  # Format the output to 9 decimal places
