
def if_perfect_num(lst):
    def is_perfect_num(n):
        divisors_sum = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors_sum += i + (n//i if i != n//i else 0)
        return divisors_sum == n
    
    if len(lst) >= 34:
        return is_perfect_num(lst[33])
    else:
        return False
