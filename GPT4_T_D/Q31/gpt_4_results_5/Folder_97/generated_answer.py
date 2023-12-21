
def if_perfect_num(num_list):
    try:
        number = num_list[132]
        divisors = [i for i in range(1,number) if number % i == 0]
        if sum(divisors) == number:
            return True
        else:
            return False
    except IndexError:
        return False
