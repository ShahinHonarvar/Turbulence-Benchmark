
def if_perfect_num(lst):
    try:
        number = lst[64]
        sum_of_divisors = sum([i for i in range(1, number) if number % i == 0])
        return sum_of_divisors == number
    except IndexError:
        return False
