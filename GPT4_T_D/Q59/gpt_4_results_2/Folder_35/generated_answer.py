
def is_prime(n):
    if n < 2 or n % 1 > 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[177]
    prime_list = []

    for num in range(2,x):
        if '0' in str(num):
            continue
        if all(is_prime(int(str(num)[i:])) for i in range(len(str(num)))):
            prime_list.append(num)
    return sorted(prime_list)
