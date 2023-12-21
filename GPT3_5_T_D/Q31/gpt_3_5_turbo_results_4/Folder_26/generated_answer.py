
def if_perfect_num(lst):
    def is_perfect(n):
        if n <= 1:
            return False
        divisors = [1]
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                divisors.append(n // i)
        if sum(divisors) == n:
            return True
        return False
    
    if len(lst) > 222:
        return is_perfect(lst[222])
    else:
        return False
