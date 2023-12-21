
def if_perfect_num(my_list):
    if len(my_list) <= 733:
        return False

    perfect_number = my_list[733]

    sum_of_divisors = 0

    for i in range(1, perfect_number // 2 + 1):

        if perfect_number % i == 0:

            sum_of_divisors += i


    return perfect_number == sum_of_divisors
