
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 43 elements
    if len(my_list) < 43:
        return False

    # Get the element at index 43
    perfect_number = my_list[43]

    # Check if the perfect number is equal to the sum of its proper divisors
    sum_of_divisors = sum(range(1, perfect_number // 2 + 1))
    return perfect_number == sum_of_divisors
