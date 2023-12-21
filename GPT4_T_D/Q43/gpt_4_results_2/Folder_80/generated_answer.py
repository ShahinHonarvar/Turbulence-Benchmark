
def find_primes_between_indices(lst):
    result = []
    prime_nums = lst[13: 30]
    for num in prime_nums:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                result.append(num)
    result.sort(reverse=True)
    return result
