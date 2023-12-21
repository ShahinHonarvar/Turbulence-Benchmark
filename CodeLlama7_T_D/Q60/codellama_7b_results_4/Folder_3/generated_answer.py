
def all_left_right_truncatable_prime(x):
    # create an empty list to store the results
    result = []

    # loop over the numbers from 1 to x, inclusive
    for i in range(1, x + 1):
        # check if i is a prime number
        if is_prime(i):
            # create a copy of i
            j = i

            # loop while j is greater than 0 and is divisible by 10
            while j > 0 and j % 10 == 0:
                # remove the last rightmost digit from j
                j //= 10

            # check if j is equal to i
            if j == i:
                # add i to the result list
                result.append(i)

    # return the result list, sorted in ascending order
    return sorted(result)
