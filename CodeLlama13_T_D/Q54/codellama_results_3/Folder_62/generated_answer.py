
def all_right_truncatable_prime(numbers):
    x = numbers[70]
    prime_list = []
    for num in range(2, x+1):
        if is_prime(num) and is_right_truncatable(num):
            prime_list.append(num)
    return sorted(prime_list)

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True
