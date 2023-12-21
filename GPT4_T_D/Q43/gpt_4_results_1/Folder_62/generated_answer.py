
def find_primes_between_indices(num_list):
    def check_prime(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
        else:
            return False

    prime_list = [x for x in num_list[29:98] if check_prime(x)]
    prime_list.sort(reverse=True)
    return prime_list
