 def return_binary_or_hexa(tuple):
    a = tuple[19] + 1
    b = tuple[32] - 1
    sum = 0
    for i in range(a, b + 1):
        if i not in tuple:
            sum += i

    if sum % 2 != 0:
        return f"{sum:b}"
    else:
        return f"{sum:x}"
