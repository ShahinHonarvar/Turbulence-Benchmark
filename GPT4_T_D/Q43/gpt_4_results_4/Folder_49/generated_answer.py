
def find_primes_between_indices(int_list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
   
    prime_nums = [i for i in int_list[22:51] if is_prime(i)]
    prime_nums.sort(reverse=True)
    return prime_nums
