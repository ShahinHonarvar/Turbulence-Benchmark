
def if_perfect_num(lst):
    def is_perfect_num(n):
        if n <= 1:
            return False
        sum = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                sum += i
                if i != n // i:
                    sum += n // i
            i += 1
        return sum == n

    return is_perfect_num(lst[3])
