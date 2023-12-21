def sum_of_divisors_in_range(x):
    divisors = []
    for i in range(58, x + 1):
        for j in range(i + 1, x + 1):
            if i * i == j * j:
                divisors.append(i * j)
            elif i * i == j * (j - 1):
                divisors.append(i * j)
            elif i * (i - 1) == j * j:
                divisors.append(i * (j - 1))
            elif i * (i - 1) == j * (j - 1):
                divisors.append(i * (j - 1))
    return sum(divisors)
