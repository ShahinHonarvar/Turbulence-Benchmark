
from math import sqrt

def find_primes_between_indices(int_list):
    prime_numbers = []
    for i in range(24,33):
        if i < len(int_list):
            num = int_list[i]
            if num > 1: 
                for j in range(2, int(sqrt(num)) + 1):
                    if (num % j) == 0:
                        break
                else:
                    prime_numbers.append(num)
    prime_numbers.sort(reverse=True)
    return prime_numbers
