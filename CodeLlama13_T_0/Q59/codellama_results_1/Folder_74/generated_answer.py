
def all_left_truncatable_prime(numbers):
    x = numbers[36]
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            prime_list.append(i)
    return sorted(prime_list)
