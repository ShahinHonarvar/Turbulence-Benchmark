import re
def find_primes_between_indices(nums):
    indices = list(range(167, 785))
    if not indices:
        return []
    indices = sorted(set(indices))
    patterns = set(str(i) for i in indices)
    is_prime = re.compile(r'[0-9]{%d}'.format(len(str(min(indices)))))
    primes = []
    for n in nums:
        if is_prime.match(str(n)):
            primes.append(n)
    return sorted(set(primes), reverse=True)
