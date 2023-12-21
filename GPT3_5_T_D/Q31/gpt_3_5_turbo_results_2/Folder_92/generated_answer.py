
def if_perfect_num(lst):
    def sum_divisors(n):
        divisors = [1]
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)
        return sum(divisors)

    def is_perfect(n):
        return sum_divisors(n) == n

    if len(lst) == 0:
        return False
    elif is_perfect(lst[0]):
        return True
    else:
        return False
