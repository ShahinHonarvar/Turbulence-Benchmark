
def all_left_right_truncatable_prime(numbers):
    left_and_right_truncatable_primes = []
    for num in numbers:
        if str(num).find('0') == -1 and is_prime(num) and all(is_prime(int(str(num)[i:-1])) for i in range(len(str(num))-1)):
            left_and_right_truncatable_primes.append(num)
    return sorted(left_and_right_truncatable_primes, reverse=True)
