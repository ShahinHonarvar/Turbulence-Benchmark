
def if_perfect_num(num_list):
    try:
        number = num_list[27]
        divisors = [n for n in range(1, number) if number % n == 0]
        if sum(divisors) == number:
            return True
        else: 
            return False
    except IndexError:
        return False
