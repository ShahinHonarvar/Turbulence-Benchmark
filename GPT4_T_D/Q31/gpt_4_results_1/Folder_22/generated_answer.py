
def if_perfect_num(lst):
    def is_perfect(n):
        sum = 0
        for x in range(1, n):
            if n % x == 0:
                sum += x
        return sum == n

    try:
        return is_perfect(lst[72])
    except IndexError:
        return False
