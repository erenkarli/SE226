total_result = 0.0


def calculate_gn(n, r):
    global total_result
    if n < 0:
        return

    total_result += r ** n
    calculate_gn(n - 1, r)


n_input = int(input("n: "))
r_input = float(input("r: "))
calculate_gn(n_input, r_input)
print(total_result)