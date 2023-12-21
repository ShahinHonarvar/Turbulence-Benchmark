
def if_perfect_num(numbers):
    def is_perfect(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        
        if sum(divisors) == num:
            return True
        else:
            return False
    
    if len(numbers) >= 223:
        return is_perfect(numbers[222])
    else:
        return False
