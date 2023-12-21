
def if_perfect_num(lst):
    def is_perfect(num):
        if num == 1:
            return False
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num
    
    if len(lst) > 60:
        return is_perfect(lst[60])
    else:
        return False
