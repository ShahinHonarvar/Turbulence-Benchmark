
def if_perfect_num(integer_list):
    def is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n

    if len(integer_list) > 94:
        return is_perfect(integer_list[94])
    else:
        return False
