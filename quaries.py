
# from fractions import Fraction
#
# def arrayfill(n):
#     return [0] * n
#
# def update_happiness(happiness, salary, index, old_salary, new_salary):
#     if new_salary > old_salary:
#         happiness[index] += 1
#     elif new_salary < old_salary:
#         happiness[index] -= 1
#
# def type_0_update(salary, happiness, l, r, c):
#     for i in range(l-1, r):
#         old_salary = salary[i]
#         salary[i] = c
#         update_happiness(happiness, salary, i, old_salary, c)
#
# def type_1_update(salary, happiness, l, r, c):
#     for i in range(l-1, r):
#         old_salary = salary[i]
#         salary[i] += c
#         update_happiness(happiness, salary, i, old_salary, salary[i])
#
# def type_2_query(salary, l, r):
#     total_salary = sum(salary[l-1:r])
#     count = r - (l - 1)
#     fraction = Fraction(total_salary, count)
#     return f"{fraction.numerator}/{fraction.denominator}"
#
# def type_3_query(happiness, l, r):
#     total_happiness = sum(happiness[l-1:r])
#     count = r - (l - 1)
#     fraction = Fraction(total_happiness, count)
#     return f"{fraction.numerator}/{fraction.denominator}"
#
# def process_queries(n, q, initial_salaries, queries):
#     salary = initial_salaries[:]
#     happiness = arrayfill(n)
#     result = []
#
#     for query in queries:
#         t = query[0]
#         if t == 0:
#
#             l, r, c = query[1], query[2], query[3]
#             type_0_update(salary, happiness, l, r, c)
#         elif t == 1:
#
#             l, r, c = query[1], query[2], query[3]
#             type_1_update(salary, happiness, l, r, c)
#         elif t == 2:
#
#             l, r = query[1], query[2]
#             result.append(type_2_query(salary, l, r))
#         elif t == 3:
#
#             l, r = query[1], query[2]
#             result.append(type_3_query(happiness, l, r))
#
#     return result
#
#
# n, q = map(int, input().split())
# initial_salaries = list(map(int, input().split()))
# queries = [list(map(int, input().split())) for _ in range(q)]
#
#
# output = process_queries(n, q, initial_salaries, queries)
#
#
# for value in output:
#     print(value)


from fractions import Fraction

def arrayfill(n):
    return [0] * n

def update_happiness(happiness, old_salary, new_salary, index):
    if new_salary > old_salary:
        happiness[index] += 1
    elif new_salary < old_salary:
        happiness[index] -= 1

def apply_updates(salary, updates):
    for i in range(len(salary)):
        if updates[i] is not None:
            salary[i] = updates[i]

def process_queries(n, q, initial_salaries, queries):
    salary = initial_salaries[:]
    happiness = arrayfill(n)
    result = []
    updates = [None] * n  # Track updates for type 0

    for query in queries:
        t = query[0]
        if t == 0:  # Type 0 Update
            l, r, c = query[1] - 1, query[2], query[3]
            for i in range(l, r):
                old_salary = salary[i]
                updates[i] = c  # Mark salary to be set to c
                update_happiness(happiness, old_salary, c, i)
            apply_updates(salary, updates)

        elif t == 1:  # Type 1 Update
            l, r, c = query[1] - 1, query[2], query[3]
            for i in range(l, r):
                old_salary = salary[i]
                salary[i] += c
                update_happiness(happiness, old_salary, salary[i], i)

        elif t == 2:  # Type 2 Query
            l, r = query[1] - 1, query[2]
            total_salary = sum(salary[l:r])
            count = r - l
            fraction = Fraction(total_salary, count)
            result.append(f"{fraction.numerator}/{fraction.denominator}")

        elif t == 3:  # Type 3 Query
            l, r = query[1] - 1, query[2]
            total_happiness = sum(happiness[l:r])
            count = r - l
            fraction = Fraction(total_happiness, count)
            result.append(f"{fraction.numerator}/{fraction.denominator}")

    return result

n, q = map(int, input().split())
initial_salaries = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

output = process_queries(n, q, initial_salaries, queries)

for value in output:
    print(value)
