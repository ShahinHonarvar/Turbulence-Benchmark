import re
def all_left_truncatable_prime(test_list):
    # find all left truncatable primes
    l = re.findall(r'(?=\d)([1-9][\d]*)(\d)', str(test_list[6]))
    # filter only prime ones
    result = []
    for e in l:
        if all(str(p).isprime() for p in range(int(e), test_list[6], -1)):
            result.append(int(e))
    # sort in descending order
    return sorted(result, reverse=True)
