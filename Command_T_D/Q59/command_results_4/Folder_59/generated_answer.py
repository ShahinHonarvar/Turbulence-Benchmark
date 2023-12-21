def all_left_truncatable_prime(nums):
    # sort input in descending order
    nums = sorted(nums)[::-1]
    # define a helper function
    def is_left_truncatable_prime(n):
        # check for 0
        if n == 0:
            return False
        # check for all other non-zero digits
        for d in str(n):
            if d == '0':
                return False
            elif d not in '2357':
                return False
        # all digits are 0, 2, 3, 5 or 7
        return True
    # define the list to store the left-truncatable primes
    left_trunc_primes = []
    # loop over all input elements
    for i in range(len(nums)):
        # left-truncatable primes less than the current element
        if is_left_truncatable_prime(nums[i] - 1):
            left_trunc_prime = nums[i] - 1
            # add the prime to the list
            left_trunc_primes.append(left_trunc_prime)
    # return the list of left-truncatable primes
    return left_trunc_primes
