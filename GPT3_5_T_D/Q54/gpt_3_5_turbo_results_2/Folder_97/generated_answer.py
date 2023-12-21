
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[645]
    result = []
    for num in range(2, x):
        if is_prime(num):
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                result.append(num)
    
    return sorted(result)
