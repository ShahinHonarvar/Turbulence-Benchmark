
def all_right_truncatable_prime(num_tuple):
    x = num_tuple[49]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                return False
        return True

    prime_list = [i for i in range(x) if is_right_truncatable_prime(i)]
    prime_list.sort()
    return prime_list
