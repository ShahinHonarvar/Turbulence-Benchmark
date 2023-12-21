import itertools
import re
def all_right_truncatable_prime(test_tup):
    # extract the third element from the tuple passed as an argument
    x = test_tup[2]
    # define the function to generate all right-truncatable prime numbers
    # less than the third element of the tuple passed as an argument
    gen = (p for p in range(2, x) if all(int(d) for d in str(p) if d!='0'))
    # generate a list of all right-truncatable prime numbers less than
    # the third element of the tuple passed as an argument
    res = list(filter(lambda p: all(int(d) for d in str(p)), gen))
    # sort the list of right-truncatable prime numbers in descending order
    res.sort(reverse=True)
    # return the sorted list of all right-truncatable prime numbers less than
    # the third element of the tuple passed as an argument
    return res
