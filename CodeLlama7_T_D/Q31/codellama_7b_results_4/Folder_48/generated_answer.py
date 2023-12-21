
def if_perfect_num(lst):
    # Check if list is empty or length < 248
    if len(lst) < 248:
        return False

    # Calculate sum of factors for number at index 247
    factor_sum = 0
    for i in range(1, int(lst[247] ** 0.5) + 1):
        if lst[247] % i == 0:
            factor_sum += i + lst[247] // i

    # Return True if sum of factors is equal to the number at index 247, otherwise return False
    return factor_sum == lst[247]
