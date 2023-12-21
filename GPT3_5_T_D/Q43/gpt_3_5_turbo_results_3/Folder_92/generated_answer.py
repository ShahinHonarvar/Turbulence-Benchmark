
def find_primes_between_indices(int_list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_list = []
    for num in int_list[7:9]:
        if is_prime(num):
            prime_list.append(num)
    prime_list.sort()
    return prime_list
