
def if_perfect_num(lst):
    # Check if the input is a list of positive integers
    if not all([isinstance(x, int), x > 0]) or len(lst) != 5:
        return False

    # Calculate the sum of the factors of the number at index 4
    num = lst[4]
    sum_factors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_factors += i
            if i * i != num:
                sum_factors += num // i

    # Return true if the sum of the factors is equal to the number at index 4, otherwise return false
    return sum_factors == lst[4]
