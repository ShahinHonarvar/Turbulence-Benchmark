
def all_left_right_truncatable_prime(t):
    x = t[945]
    primes = [2]
    truncs = []

    # Create a list of primes upto x
    for num in range(3, x+1, 2):
        if all(num%i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)

    # Check for left and right truncatable primes
    for prime in primes:
        str_prime = str(prime)
        if "0" not in str_prime:
            truncatable_prime = True
            for i in range(1, len(str_prime)):
                left = int(str_prime[i:]) in primes
                right = int(str_prime[:-i]) in primes
                if not left or not right:
                    truncatable_prime = False
                    break
            if truncatable_prime:
                truncs.append(prime)
    
    # Returning sorted truncatable primes in descending order
    return sorted(truncs, reverse=True)
