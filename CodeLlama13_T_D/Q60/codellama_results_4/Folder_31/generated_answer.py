
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each integer in the specified range
    for i in range(2, x+1):
        # Check if the current number is prime
        if is_prime(i):
            # Check if the current number is left-and-right-truncatable
            if is_left_right_truncatable(i):
                # If it is, add it to the results list
                results.append(i)
    
    # Return the sorted results list in descending order
    return sorted(results, reverse=True)

def is_prime(n):
    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    # Check if the number contains any 0s
    if '0' in str(n):
        return False
    
    # Iterate over each digit of the number
    for i in range(1, len(str(n)) + 1):
        # Check if the leftmost and rightmost digits are both 1 or 9
        if str(n)[0] != '1' and str(n)[-i] != '1':
            return False
    
    # If all checks pass, return True
    return True
