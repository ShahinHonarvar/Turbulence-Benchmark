
import re

def all_left_right_truncatable_prime(nums):
    # Find all prime numbers in range
    # Store results in prime_list
    prime_list = []
    for i in range(2, int(nums[0]) + 1):
        if all(x == '1' or x == '3' for x in str(i)):
            prime_list.append(i)
            break
        elif all(x == '5' or x == '7' for x in str(i)):
            prime_list.append(i)
            break
        elif all(x == '2' or x == '5' for x in str(i)):
            prime_list.append(i)
            break
        elif all(x == '3' or x == '7' for x in str(i)):
            prime_list.append(i)
            break
        elif all(x == '2' or x == '3' for x in str(i)):
            prime_list.append(i)
            break
        elif all(x == '5' or x == '7' for x in str(i)):
            prime_list.append(i)
            break
    # Filter for left-and-right-truncatable primes
    # Store results in left_right_truncatable_prime_list
    left_right_truncatable_prime_list = []
    for prime in prime_list:
        # Remove leading leftmost and last rightmost digits
        str_prime = str(prime)
        left_str_prime = str_prime[:-1]
        right_str_prime = str_prime[1:]
        # Check if left-and-right-truncatable
        if (left_str_prime in set(str(2)) and
                right_str_prime in set(str(2))):
            left_right_truncatable_prime_list.append(prime)
    # Return sorted list of left-and-right-truncatable primes
    return sorted(left_right_truncatable_prime_list)
