
def all_right_truncatable_prime(numbers):
    x = numbers[30]
    prime_list = []
    for num in range(10, x+1):
        if is_right_truncatable_prime(num):
            prime_list.append(num)
    return sorted(prime_list, reverse=True)

def is_right_truncatable_prime(num):
    if num % 2 == 0 or num % 5 == 0:
        return False
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
