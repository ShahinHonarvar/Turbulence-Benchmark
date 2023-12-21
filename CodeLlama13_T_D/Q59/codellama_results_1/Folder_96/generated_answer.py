
def all_left_truncatable_prime(numbers):
    left_truncatable_primes = []
    for number in numbers:
        if str(number)[1:] == "0":
            continue
        for i in range(len(str(number)) - 1):
            new_num = int(str(number)[:-i])
            if not is_prime(new_num):
                break
            left_truncatable_primes.append(new_num)
    return sorted(left_truncatable_primes)
