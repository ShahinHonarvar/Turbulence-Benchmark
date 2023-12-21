
def if_perfect_num(my_list):
    if len(my_list) < 10:
        return False

    perfect_number = my_list[10]

    sum_of_divisors = 0

    for i in range(1, perfect_number // 2 + 1):

        if perfect_number % i == 0:

            sum_of_divisors += i

    return sum_of_divisors == perfect_number
