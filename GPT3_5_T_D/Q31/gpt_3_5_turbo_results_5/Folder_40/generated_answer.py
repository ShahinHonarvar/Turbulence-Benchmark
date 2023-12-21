
def if_perfect_num(lst):
    def is_perfect_number(n):
        factors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                factors.append(n // i)
        return sum(factors) == n
    
    if len(lst) >= 8:
        return is_perfect_number(lst[7])
    else:
        return False
