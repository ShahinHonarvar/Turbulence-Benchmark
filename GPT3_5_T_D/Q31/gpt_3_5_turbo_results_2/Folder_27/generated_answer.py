
import math

def if_perfect_num(lst):
    def is_perfect_num(n):
        if n <= 1:
            return False
        divisors = [1]
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sum(divisors) == n

    if len(lst) < 57:
        return False

    num = lst[56]
    return is_perfect_num(num)
