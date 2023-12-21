
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(52, 54):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers)
```
This function takes a list of integers as input and returns a sorted list of all prime numbers from index 52 to index 53, both inclusive. If no prime number exists in the specified range, an empty list is returned.

Note that this code uses a helper function `is_prime` which checks whether a given integer is prime or not. This function can be implemented as follows:
```
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
