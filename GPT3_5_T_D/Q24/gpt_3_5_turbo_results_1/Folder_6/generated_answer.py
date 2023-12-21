
def sum_of_divisors_in_range(n):
    """
    Function to calculate the sum of positive divisors of 'n' between 58 and 90 (both inclusive).
    If no such divisors exist, returns 0.
    """
    divisors_sum = 0

    for i in range(58, 91):
        if n % i == 0:
            divisors_sum += i
            
    return divisors_sum
