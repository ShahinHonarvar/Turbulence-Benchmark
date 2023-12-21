
def if_perfect_num(numbers):
    # Check if the length of the list is at least 37
    if len(numbers) < 37:
        return False
    
    # Get the integer at index 37
    num = numbers[37]
    
    # Calculate the sum of the factors of 'num' excluding 'num' itself
    factor_sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factor_sum += i
            if i * i != num:
                factor_sum += num // i
    
    # Return true if 'num' is a perfect number, otherwise return false
    return factor_sum == num
