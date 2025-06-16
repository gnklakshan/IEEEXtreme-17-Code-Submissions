import sys
import math
from fractions import Fraction

input = sys.stdin.read


class SegmentTree:
    def __init__(self, data, func, default=0):
        self.n = len(data)
        self.func = func
        self.default = default
        self.tree = [default] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, l, r, value, add=False):
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                self.tree[l] = self.func(self.tree[l], value) if add else value
                l += 1
            if r & 1:
                r -= 1
                self.tree[r] = self.func(self.tree[r], value) if add else value
            l //= 2
            r //= 2
        self.build([self.tree[i] for i in range(self.n, 2 * self.n)])

    def query(self, l, r):
        res = self.default
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = self.func(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.func(res, self.tree[r])
            l //= 2
            r //= 2
        return res


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    data = input().strip().split()
    index = 0
    N = int(data[index])
    Q = int(data[index + 1])
    index += 2

    salaries = [int(data[i]) for i in range(index, index + N)]
    index += N

    # Happiness array initially set to zero
    happiness = [0] * N

    salary_tree = SegmentTree(salaries, lambda x, y: x + y)
    happiness_tree = SegmentTree(happiness, lambda x, y: x + y)

    results = []

    for _ in range(Q):
        t = int(data[index])
        l = int(data[index + 1]) - 1
        r = int(data[index + 2])

        if t == 0:
            c = int(data[index + 3])
            index += 4
            current_salaries = salary_tree.query(l, r)
            for i in range(l, r):
                current_salary = salary_tree.query(i, i + 1)
                if current_salary != c:
                    happiness_tree.update(i, i + 1, happiness_tree.query(i, i + 1) + 1)
            salary_tree.update(l, r, c)
        elif t == 1:
            c = int(data[index + 3])
            index += 4
            for i in range(l, r):
                salary_tree.update(i, i + 1, salary_tree.query(i, i + 1) + c, add=True)
                if c != 0:
                    happiness_tree.update(i, i + 1, happiness_tree.query(i, i + 1) + 1)
        elif t == 2:
            index += 3
            total_salary = salary_tree.query(l, r)
            range_length = r - l
            avg_salary = Fraction(total_salary, range_length)
            results.append(f"{avg_salary.numerator}/{avg_salary.denominator}")
        elif t == 3:
            index += 3
            total_happiness = happiness_tree.query(l, r)
            range_length = r - l
            avg_happiness = Fraction(total_happiness, range_length)
            results.append(f"{avg_happiness.numerator}/{avg_happiness.denominator}")

    print("\n".join(results))


if __name__ == "__main__":
    main()
