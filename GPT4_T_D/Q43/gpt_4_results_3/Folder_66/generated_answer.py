
def find_primes_between_indices(lst):
    result = []
    if len(lst) >= 73:
        for num in lst[72:73]:
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    result.append(num)
    return sorted(result)
