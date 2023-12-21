
def sum_of_divisors_in_range(n):
    # Calculate the sum of divisors between 10 and 55
    div_sum = 0
    for i in range(10, 56):
        if n % i == 0:
            div_sum += i
            
    return div_sum
