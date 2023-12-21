
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    x = numbers[54]
    result = []
    for n in range(int(x ** 0.5) + 1):
        if is_prime(n):
            num = str(n)
            while num:
                if not is_prime(int(num)):
                    break
                num = num[:-1]
            else:
                result.append(n)
    
    return sorted(result)
