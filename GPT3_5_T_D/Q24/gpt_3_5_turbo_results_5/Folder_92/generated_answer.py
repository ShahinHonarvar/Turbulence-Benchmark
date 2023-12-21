
def sum_of_divisors_in_range(num):
    if num < 1:
        return 0
    
    divisors = []
    for i in range(1, num+1):
        if num % i == 0 and 8 <= i <= 9:
            divisors.append(i)
    
    return sum(divisors)
