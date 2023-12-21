
def if_perfect_num(num_list):
    if len(num_list) > 16:
        number = num_list[16]
        divisors = [i for i in range(1, number) if number % i == 0]
        return sum(divisors) == number
    return False
