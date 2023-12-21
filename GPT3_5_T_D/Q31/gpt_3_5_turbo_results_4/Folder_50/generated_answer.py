
def if_perfect_num(lst):
    def is_perfect(num):
        divisors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        return sum(divisors) == num
    
    if len(lst) >= 41:
        return is_perfect(lst[40])
    else:
        return False
