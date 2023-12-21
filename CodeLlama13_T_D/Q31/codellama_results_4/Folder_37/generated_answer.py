
def if_perfect_num(list_of_ints):
    if len(list_of_ints) < 29:
        return False
    else:
        n = list_of_ints[28]
        sum_factors = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                sum_factors += i
                if n // i != i:
                    sum_factors += n // i
        return sum_factors == n
