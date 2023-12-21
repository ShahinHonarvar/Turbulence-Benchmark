
def if_perfect_num(lst):
    number = lst[69]
    sum_of_factors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_factors += i
    return sum_of_factors == number
