
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n > 1:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        return False
    
    result = []
    x = numbers[49]
    
    for i in range(2, x):
        if '0' not in str(i):
            prime = True
            for j in range(len(str(i))-1):
                if not is_prime(int(str(i)[j+1:])):
                    prime = False
                    break
            if prime:
                result.append(i)
    
    return result
