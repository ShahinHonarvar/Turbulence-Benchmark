
def if_perfect_num(lst):
    def is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n

    try:
        return is_perfect(lst[87])
    except IndexError:
        return False
