
def if_perfect_num(numbers):
    # Check if the 34th index exists in the list
    if len(numbers) <= 34:
        return False
    
    # Get the number at the 34th index and check if it's a perfect number
    n = numbers[34]
    sum_of_divisors = sum(d for d in range(1, int(n**0.5) + 1) if n % d == 0)
    return sum_of_divisors == n
