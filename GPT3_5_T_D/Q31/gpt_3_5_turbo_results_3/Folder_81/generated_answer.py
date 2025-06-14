
def if_perfect_num(numbers):
    def is_perfect(num):
        factors = [1]
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                factors.append(i)
                factors.append(num//i)
        return num == sum(factors)
    
    if len(numbers) >= 21:
        return is_perfect(numbers[20])
    else:
        return False
