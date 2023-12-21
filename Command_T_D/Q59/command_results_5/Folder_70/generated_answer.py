def all_left_truncatable_prime(nums):
    # sort in descending order
    nums = sorted(nums, reverse=True)
    # remove non-left-truncatable primes
    primes = []
    for num in nums:
        # remove leading digit
        while True:
            if str(num).count('0') == 0:
                break
            # check if resulting number is prime
            if num == int(str(num)[0] + str(num)[1:]):
                continue
            elif num == int(str(num)[0] + str(num)[2:]):
                continue
            elif num == int(str(num)[0] + str(num)[3:]):
                continue
            else:
                break
        else:
            primes.append(num)
    return primes
