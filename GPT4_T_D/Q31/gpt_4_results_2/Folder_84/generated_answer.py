
def if_perfect_num(integer_list):
    if len(integer_list) > 685:
        number = integer_list[685]
        sum_of_divisors = 0
        for i in range(1, number):
            if number % i == 0:
                sum_of_divisors += i
        if sum_of_divisors == number:
            return True
    return False
