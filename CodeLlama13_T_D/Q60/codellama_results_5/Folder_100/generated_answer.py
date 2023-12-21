
def all_left_right_truncatable_prime(numbers):
    x = numbers[26]
    prime_list = []
    for i in range(x):
        if is_prime(i) and no_zeros(str(i)):
            prime_list.append(i)
    return prime_list
