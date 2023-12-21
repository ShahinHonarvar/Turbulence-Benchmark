
def sum_of_divisors_in_range(n):
    if n <= 0:
        return "Input must be a positive integer"
    else:
        sum_of_divisors = 0
        for i in range(224, 585):
            if n % i == 0:
                sum_of_divisors += i 
        return sum_of_divisors
