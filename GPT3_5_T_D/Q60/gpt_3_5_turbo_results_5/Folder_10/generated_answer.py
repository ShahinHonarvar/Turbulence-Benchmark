
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[38]
    result = []
    for num in range(x, 1, -1):
        if '0' in str(num):
            continue
            
        left_truncatable = True
        right_truncatable = True
        
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                right_truncatable = False
            if not is_prime(int(str(num)[:i+1])):
                left_truncatable = False
                
        if left_truncatable and right_truncatable:
            result.append(num)
            
    return sorted(result, reverse=True)
