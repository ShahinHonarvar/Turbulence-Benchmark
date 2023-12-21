
def find_second_largest_num(numbers):
    # get the sublist from index 21 to index 97
    sublist = numbers[21:98]
    # sort the sublist in descending order
    sublist.sort(reverse=True)
    # check if there is a second largest element
    if len(sublist) > 1:
        return sublist[1]
    else:
        return None
