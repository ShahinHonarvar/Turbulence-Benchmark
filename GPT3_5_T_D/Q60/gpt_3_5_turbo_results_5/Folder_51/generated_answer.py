
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[54]
    truncatable_primes = []
    
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        prime = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])) or not is_prime(int(str(num)[:i + 1])):
                prime = False
                break
        if prime:
            truncatable_primes.append(num)
    
    return truncatable_primes
