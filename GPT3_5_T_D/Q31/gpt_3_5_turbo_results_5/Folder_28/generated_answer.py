
def if_perfect_num(lst):
    def sum_of_divisors(n):
        divisors = []
        for i in range(1, int(n/2) + 1):
            if n % i == 0:
                divisors.append(i)
        return sum(divisors)
    
    if len(lst) > 37 and sum_of_divisors(lst[37]) == lst[37]:
        return True
    else:
        return False
