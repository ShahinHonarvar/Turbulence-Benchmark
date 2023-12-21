
def if_perfect_num(lst):
    def is_perfect_num(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        if sum(divisors) == num:
            return True
        else:
            return False
    
    return is_perfect_num(lst[459])
