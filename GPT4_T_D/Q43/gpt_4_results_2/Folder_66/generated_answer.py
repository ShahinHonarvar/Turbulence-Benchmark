
def find_primes_between_indices(lst):
    def is_prime(n):
        if n<2:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        return True

    if len(lst) >= 73:
        sub_lst = lst[72:73]
        primes = [num for num in sub_lst if is_prime(num)]
    else:
        primes = []

    return sorted(primes)
