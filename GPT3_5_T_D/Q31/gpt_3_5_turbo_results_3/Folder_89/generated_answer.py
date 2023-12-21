
def if_perfect_num(lst):
    def is_perfect(n):
        factors = [1]
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)
                factors.append(n // i)
        if sum(factors) == n:
            return True
        return False

    return is_perfect(lst[18]) if len(lst) > 18 else False
