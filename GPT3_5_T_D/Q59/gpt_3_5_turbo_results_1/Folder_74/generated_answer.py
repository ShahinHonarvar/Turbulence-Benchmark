
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    x = numbers[36]
    result = []
    for num in range(10, x):
        if '0' in str(num):
            continue
        prime = True
        truncated = str(num)
        while truncated:
            if not is_prime(int(truncated)):
                prime = False
                break
            truncated = truncated[1:]
        if prime:
            result.append(num)
        
    return sorted(result)
