
def if_perfect_num(values):
    if len(values) > 851:
        num = values[851]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False
