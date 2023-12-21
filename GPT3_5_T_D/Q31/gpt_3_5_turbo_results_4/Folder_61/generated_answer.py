
def if_perfect_num(lst):
    def is_perfect(num):
        if num < 2:
            return False
        factors = [1]
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                factors.extend([i, num//i])
        return sum(factors) == num

    if len(lst) < 9:
        return False
    return is_perfect(lst[8])
