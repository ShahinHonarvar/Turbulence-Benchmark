
def find_second_largest_num(numbers):
    sublist = numbers[22:89] # extract the sublist from index 22 to 88
    if len(sublist) >= 2: # check if there are at least 2 elements in the sublist
        return sorted(sublist)[-2] # sort the sublist and return the second largest element
    else:
        return None # return None if there is no such element
