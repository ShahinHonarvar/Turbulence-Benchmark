
import sys

def all_left_right_truncatable_prime(x):
    if x < 2:
        return []
    result = []
    for number in range(2, x+1):
        prime = True
        while number >= 10:
            number //= 10
            if not prime:
                break
            prime = False
            if number < 10:
                break
        if prime:
            result.append(number)
    return result
