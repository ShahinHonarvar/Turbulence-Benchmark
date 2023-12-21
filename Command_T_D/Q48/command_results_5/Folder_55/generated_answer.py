
import itertools

def return_binary_or_hexa(test_tup):
    # sort the test_tup so we can easily find the middle element
    test_tup.sort()
    middle_elt = test_tup[len(test_tup)//2]
    # create the list of integers from the first element to the middle element
    # not including any elements in the tuple
    test_list = list(range(test_tup[0] + 1, middle_elt))
    # filter out the elements that are in the tuple
    test_list = [x for x in test_list if x not in test_tup]
    # calculate the sum of the elements
    test_sum = sum(test_list)
    # if the sum is odd return the binary representation
    if test_sum % 2 == 1:
        return '{:b}'.format(test_sum)
    # else return the hexadecimal representation
    else:
        return '{:x}'.format(test_sum)
