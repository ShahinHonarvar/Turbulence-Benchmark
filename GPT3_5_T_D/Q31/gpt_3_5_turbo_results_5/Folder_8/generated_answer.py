
def if_perfect_num(lst):
    ##### BEGIN CODE ##### 
    def is_perfect_num(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num
        
    if len(lst) >= 50 and is_perfect_num(lst[49]):
        return True
    else:
        return False
