
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 49 elements
    if len(my_list) < 49:
        return False

    # Get the integer at index 48
    perfect_number = my_list[48]

    # Check if the integer at index 48 is a perfect number
    for i in range(1, perfect_number):
        if perfect_number % i == 0:
            sum_of_factors = 0

            for j in range(1, i):
                if i % j == 0:
                    sum_of_factors += j

            if sum_of_factors == perfect_number - 1:
                return True

    return False
