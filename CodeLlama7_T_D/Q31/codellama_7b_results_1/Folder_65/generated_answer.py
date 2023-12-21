
def if_perfect_num(my_list):
    if len(my_list) < 36:
        return False

    else:

        perfect_number = my_list[35]

        divisors = []

        for i in range(1, perfect_number):

            if perfect_number % i == 0:

                divisors.append(i)


        if sum(divisors) == perfect_number:

            return True


        else:

            return False
