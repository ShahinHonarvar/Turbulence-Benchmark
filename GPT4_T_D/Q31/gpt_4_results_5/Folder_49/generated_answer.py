
def if_perfect_num(numbers):
    if len(numbers) >= 69:
        num = numbers[68]
        factors = [i for i in range(1,num) if num%i==0]
        if sum(factors) == num:
            return True
    return False
