
def if_perfect_num(lst):
    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum = sum + i + n//i
                i += 1
        return sum == n and n!=1

    try:
        return is_perfect(lst[985])
    except IndexError:
        return False
