
def if_perfect_num(lst):
    def is_perfect(n):
        total = 0
        for i in range(1, n):
            if n % i == 0:
                total += i
        return total == n

    return is_perfect(lst[84]) if len(lst) > 84 else False
