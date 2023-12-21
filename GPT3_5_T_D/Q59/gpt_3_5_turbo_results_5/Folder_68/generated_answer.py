
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[1]
    result = []
    for num in range(x-1, 0, -1):
        if not '0' in str(num):
            is_left_truncatable_prime = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime:
                result.append(num)
    return result
