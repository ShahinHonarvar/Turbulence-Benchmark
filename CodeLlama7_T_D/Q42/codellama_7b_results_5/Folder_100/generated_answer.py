
def prime_factors(my_list):
    # find the number at index 99
    target_number = my_list[99]
    # initialize an empty set to store prime factors
    prime_factors = set()
    # iterate through the list of numbers
    for num in my_list:
        # check if the current number is a factor of the target number
        if target_number % num == 0:
            # if it is, add it to the set of prime factors
            prime_factors.add(num)
    # return the set of prime factors
    return prime_factors
