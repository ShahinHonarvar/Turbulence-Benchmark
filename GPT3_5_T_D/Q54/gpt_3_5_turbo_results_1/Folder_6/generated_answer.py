
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) < 75:
        return []
    
    x = numbers[74]
    result = []
    
    for num in range(2, x):
        if is_prime(num):
            right_truncatable = True
            temp = num
            while temp > 10:
                temp = int(temp / 10)
                if not is_prime(temp):
                    right_truncatable = False
                    break
            if right_truncatable:
                result.append(num)
    
    result.sort()
    return result
