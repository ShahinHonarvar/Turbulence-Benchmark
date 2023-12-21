
def find_primes_between_indices(int_list):
    def check_prime(num):
        if num < 2:
            return False
        for i in range(2,num):
            if (num % i) == 0:
                return False
        return True
    
    prime_list = [num for num in int_list[167:786] if check_prime(num)]
    prime_list.sort(reverse=True)
    return prime_list
