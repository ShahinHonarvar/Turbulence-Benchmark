import itertools
def prime_factors(nums):
    return set(itertools.chain.from_iterable(
        [
            [x for x in range(2, int(num ** .5) + 1) if num % x == 0],
            [num // x for x in range(2, int(num ** .5) + 1) if num % x == 0],
        ]
        for num in nums
    ))
