
def if_perfect_num(lst):
    def is_perfect_num(n):
        if n == 1:
            return False
        divisors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sum(divisors) == n
        
    if len(lst) > 97 and is_perfect_num(lst[97]):
        return True
    else:
        return False
