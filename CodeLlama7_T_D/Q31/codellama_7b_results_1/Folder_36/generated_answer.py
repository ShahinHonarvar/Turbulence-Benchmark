
def if_perfect_num(my_list):
    # Check if the list has more than 1000 elements
    if len(my_list) < 990:
        return False

    perfect_number = my_list[990]

    # Check if the number is a perfect number

    for i in range(1, perfect_number // 2 + 1):

        if perfect_number % i == 0:

            sum_of_divisors = i + (perfect_number // i)

            if sum_of_divisors == perfect_number:

                return True


    return False
