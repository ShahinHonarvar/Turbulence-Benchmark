
def if_perfect_num(lst):
    # Check if the list is empty
    if len(lst) == 0:
        return False

    # Check if the integer at index 59 is a perfect number
    if lst[59] == 0 or lst[59] % 2 != 0:
        return False

    # Calculate the sum of the factors of the integer at index 59
    sum_factors = 0
    for i in range(1, int(lst[59]) / 2 + 1):
        if lst[59] % i == 0:
            sum_factors += i

    # Return true if the integer at index 59 is a perfect number, otherwise return false
    return lst[59] == sum_factors
