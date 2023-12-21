
def find_primes_between_indices(lst):
    primes_list = []
    for num in lst[229:851]:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes_list.append(num)
    return sorted(primes_list, reverse=True)
