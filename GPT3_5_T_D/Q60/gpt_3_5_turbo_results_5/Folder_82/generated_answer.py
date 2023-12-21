
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        if x < 10:
            continue
        x_str = str(x)
        if '0' in x_str:
            continue
        
        if is_prime(x):
            x_temp = x
            truncatable_prime = True
            while x_temp >= 10:
                x_temp = int(str(x_temp)[1:-1])
                if not is_prime(x_temp):
                    truncatable_prime = False
                    break
            if truncatable_prime:
                result.append(x)
    
    return sorted(result, reverse=True)
