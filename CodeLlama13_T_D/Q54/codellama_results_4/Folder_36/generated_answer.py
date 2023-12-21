
def all_right_truncatable_prime(numbers):
    x = numbers[992]
    prime_list = []
    for num in range(x):
        if is_right_truncatable_prime(num):
            prime_list.append(num)
    return sorted(prime_list)

def is_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    for i in range(len(str(num))-1, 0, -1):
        if not is_prime(int(str(num)[:i])):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
