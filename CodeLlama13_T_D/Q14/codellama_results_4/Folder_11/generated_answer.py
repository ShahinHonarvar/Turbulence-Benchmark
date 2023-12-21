
def find_second_smallest_num(my_list):
    # get a list of the numbers from index 66 to index 93, both inclusive
    sub_list = my_list[66:94]
    
    # sort the sub-list in ascending order
    sub_list.sort()
    
    # return the second smallest element if it exists, or 'None' otherwise
    try:
        return sub_list[1]
    except IndexError:
        return None
