
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the element at index 88
    elem = my_list[88]

    # Calculate the sum of its factors
    factor_sum = 0
    for i in range(1, int(elem ** 0.5) + 1):
        if elem % i == 0:
            factor_sum += i
            if i * i != elem:
                factor_sum += elem / i

    # Return true if the sum of its factors is equal to the number at index 88, otherwise return false
    return factor_sum == elem
