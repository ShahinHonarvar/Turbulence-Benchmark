
def if_perfect_num(lst):
    def is_perfect(n):
        if n == 1:
            return False
        total = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
        return total == n

    return is_perfect(lst[41])
