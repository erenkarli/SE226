def factorial(x: int) -> int:
    if x == 0 or x == 1:
        return 1
    return factorial(x - 1) * x


abs_term = lambda x, i: (x ** (2 * i)) / factorial(2 * i)


def exp_x(x: int, n: int) -> float:
    summation = 0.0
    for i in range(n):
        summation += ((-1) ** i) * abs_term(x, i)

    absolute_res = lambda a: a if a >= 0 else -a
    return absolute_res(summation)


n_val = int(input("n: "))
x_val = int(input("x: "))
print(exp_x(x_val, n_val))