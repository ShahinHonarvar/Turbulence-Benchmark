
def if_perfect_num(lst):
    def is_perfect_number(n):
        if n <= 0:
            return False
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n

    return is_perfect_number(lst[94])
