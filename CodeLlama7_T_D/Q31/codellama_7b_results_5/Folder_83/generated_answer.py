
def if_perfect_num(my_list):
    # Check if the list has at least 95 elements
    if len(my_list) < 95:
        return False

    # Check if the integer at index 95 is a perfect number
    perfect_number = my_list[95]
    divisors = []

    for i in range(1, perfect_number):
        if perfect_number % i == 0:
            divisors.append(i)

    sum_of_divisors = sum(divisors)

    if sum_of_divisors == perfect_number:
        return True

    else:

        return False
