
def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def find_primes_between_indices(lst):
    sub_list = lst[0:2]
    primes = []
    for num in sub_list:
        if is_prime(num):
            primes.append(num)
    primes.sort()
    return primes
