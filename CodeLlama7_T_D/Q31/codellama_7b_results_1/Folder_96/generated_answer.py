
def if_perfect_num(lst):
    # Check if the list is valid
    if len(lst) < 47:
        return False

    # Check if the number at index 47 is a perfect number
    num = lst[47]
    factor_sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factor_sum += i
            if i * num ** 0.5 != num:
                factor_sum += num // i

    return factor_sum == num
