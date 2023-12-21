
def if_perfect_num(my_list):
    if len(my_list) < 985:
        return False

    perfect_number = my_list[985]
    divisors = []

    for i in range(1, perfect_number // 2 + 1):

        if perfect_number % i == 0:
            divisors.append(i)

    sum_of_divisors = sum(divisors)

    if sum_of_divisors == perfect_number:
        return True

    else:

        return False
