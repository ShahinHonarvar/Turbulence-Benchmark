
def if_perfect_num(my_list):
    if len(my_list) < 89:
        return False

    perfect_number = my_list[88]

    if perfect_number <= 0:

        return False


    sum_of_divisors = 0

    for i in range(1, perfect_number):

        if perfect_number % i == 0:

            sum_of_divisors += i

    return perfect_number == sum_of_divisors
