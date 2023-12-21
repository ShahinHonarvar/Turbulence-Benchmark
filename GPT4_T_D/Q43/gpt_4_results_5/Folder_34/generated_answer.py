
def find_primes_between_indices(lst):
    def check_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    prime_nums = [i for i in lst[56:58] if check_prime(i)]
    prime_nums.sort(reverse=True)
    return prime_nums
