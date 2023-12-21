
def all_left_truncatable_prime(numbers):
    x = numbers[93]
    prime_list = []
    for i in range(2,x+1):
        if is_prime(i) and not is_left_truncatable(i):
            prime_list.append(i)
    return prime_list
