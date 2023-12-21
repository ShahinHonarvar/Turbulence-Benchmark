
def if_perfect_num(int_list):
    if len(int_list) > 41:
        number = int_list[41]
        divisors = []
        for i in range(1, number):
            if (number % i) == 0:
                divisors.append(i)
        if sum(divisors) == number:
            return True
    return False
