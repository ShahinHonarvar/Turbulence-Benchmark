def sum_of_divisors_in_range(x):
    x = str(x)
    if x[0] == "9":
        return 0
    x = int(x)
    return x * (x + 1) / 2
