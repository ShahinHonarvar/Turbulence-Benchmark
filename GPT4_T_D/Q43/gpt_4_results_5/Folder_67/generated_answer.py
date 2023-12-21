
def find_primes_between_indices(int_list):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    prime_list = [i for i in int_list[17:80] if is_prime(i)]
    prime_list.sort(reverse=True)
    return prime_list
