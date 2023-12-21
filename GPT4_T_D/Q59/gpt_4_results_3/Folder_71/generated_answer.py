
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[22]
    output = []
    for num in range(2, x+1):
        if '0' in str(num): continue
        truncate_numbers = [str(num)[i:] for i in range(len(str(num)))]
        if all(isprime(int(tn)) for tn in truncate_numbers) and isprime(num):
            output.append(num)
    return sorted(output, reverse=True)
