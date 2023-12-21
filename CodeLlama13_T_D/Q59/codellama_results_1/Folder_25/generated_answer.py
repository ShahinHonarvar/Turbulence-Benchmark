
def all_left_truncatable_prime(numbers):
    x = numbers[92]
    prime_list = []
    for num in range(2, x+1):
        if is_prime(num) and '0' not in str(num):
            prime_list.append(num)
    return sorted(prime_list)
