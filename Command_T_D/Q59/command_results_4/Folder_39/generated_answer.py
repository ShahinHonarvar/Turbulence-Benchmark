import itertools
def all_left_truncatable_prime(nums):
    # your code here
    # sort in descending order
    return sorted(set(itertools.takewhile(
        lambda x: all(str(x)[-1] % d for d in range(2, int(str(x)[-1]) + 1)),
        itertools.permutations(nums)[30]
    )), reverse=True)
