
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the results
    results = []

    # Iterate from 1 to x-1
    for i in range(1, x-1):
        # Check if i is prime
        if is_prime(i):
            # Check if i contains no 0
            if not '0' in str(i):
                # Check if all leftmost digits of i can be successively removed
                j = i
                while True:
                    # Remove the leftmost digit of j
                    j = int(str(j)[1:]))
                    # If j is not prime, break out of the loop
                    if not is_prime(j):
                        break

                # If all leftmost digits of i can be successively removed and result in a prime number, add i to results
                if j == 1:
                    results.append(i)

    # Sort the results in descending order and return them
    return sorted(results, reverse=True)

# Check if a number is prime by iterating from 2 to its square root
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True
