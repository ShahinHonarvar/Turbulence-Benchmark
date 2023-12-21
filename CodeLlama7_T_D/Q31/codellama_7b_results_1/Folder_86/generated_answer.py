
def if_perfect_num(my_list):
    # Check if the list has at least 195 elements
    if len(my_list) < 195:
        return False

    # Calculate the sum of the factors of the number at index 194
    num = my_list[194]
    sum_of_factors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_factors += i + num / i

    # Return true if the sum of the factors is equal to the number at index 194
    return sum_of_factors == my_list[194]
