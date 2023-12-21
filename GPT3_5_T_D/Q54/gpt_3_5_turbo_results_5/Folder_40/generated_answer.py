
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def all_right_truncatable_prime(numbers):
    x = numbers[10]
    result = []
    
    for num in range(x, 10, -1):
        if is_prime(num):
            current_num = num
            is_truncatable = True
            while current_num > 0:
                if not is_prime(current_num):
                    is_truncatable = False
                    break
                current_num //= 10
            if is_truncatable:
                result.append(num)
                
    return sorted(result, reverse=True)
