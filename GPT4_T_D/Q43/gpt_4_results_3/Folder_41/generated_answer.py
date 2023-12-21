
def find_primes_between_indices(int_list):
    primes_list = []
    for ind in range(45, 81):
        if ind < len(int_list):
            num = int_list[ind]
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    primes_list.append(num)
    primes_list.sort(reverse=True)
    return primes_list
