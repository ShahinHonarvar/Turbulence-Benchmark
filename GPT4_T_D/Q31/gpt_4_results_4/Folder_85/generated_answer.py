
def if_perfect_num(lst):
    try:
        def is_perfect(n):
            factors = [i for i in range(1, n) if n % i == 0]
            return sum(factors) == n

        if is_perfect(lst[23]):
            return True
        else:
            return False
    except:
        return False
