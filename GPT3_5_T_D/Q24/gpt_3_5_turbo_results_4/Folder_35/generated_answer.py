
def sum_of_divisors_in_range(num):
    div_sum = 0
    
    for i in range(1, num+1):
        if num % i == 0 and 392 <= i <= 465:
            div_sum += i
    
    return div_sum
