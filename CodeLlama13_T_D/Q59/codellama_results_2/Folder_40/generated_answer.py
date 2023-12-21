
def all_left_truncatable_prime(numbers):
    x = numbers[10]
    prime_list = []
    for num in range(2,x):
        if is_left_truncatable_prime(num):
            prime_list.append(num)
    return sorted(prime_list, reverse=True)

def is_left_truncatable_prime(num):
    if num % 2 == 0 or num % 5 == 0:
        return False
    for i in range(1, int(len(str(num))/2)):
        if not is_prime(int(str(num)[:-i])):
            return False
    return True

def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
