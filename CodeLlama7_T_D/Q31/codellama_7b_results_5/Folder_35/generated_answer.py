
def if_perfect_num(my_list):
    if len(my_list) < 1000:
        return False

    perfect_number = my_list[993]

    if perfect_number <= 0:

        return False


    divisors = []


    for i in range(1, perfect_number):

        if perfect_number % i == 0:

            divisors.append(i)


    sum_of_divisors = sum(divisors)


    if perfect_number == sum_of_divisors:

        return True


    else:


        return False
