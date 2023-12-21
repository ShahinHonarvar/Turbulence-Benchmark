
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                is_truncatable_prime = True
                for i in range(1, len(num_str)):
                    if not is_prime(int(num_str[:i])) or not is_prime(int(num_str[-i:])):
                        is_truncatable_prime = False
                        break
                if is_truncatable_prime:
                    result.append(num)
    
    result.sort()
    return result
