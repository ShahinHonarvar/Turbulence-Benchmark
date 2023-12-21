
def if_perfect_num(arr):
    if len(arr) <= 926:
        return False
    
    num = arr[926]
    sum_divisors = 0
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            sum_divisors += i
            if num // i != i:
                sum_divisors += num // i
    
    return sum_divisors == num
