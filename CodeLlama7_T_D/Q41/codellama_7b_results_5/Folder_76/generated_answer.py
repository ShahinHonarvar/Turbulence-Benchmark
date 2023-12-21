
def identical_elements(list1, list2):
    # Initialize an empty set to store the identical elements
    identical_set = set()
    # Iterate through the lists and check for identical elements
    for i in range(686, 987+1):
        if list1[i] == list2[i]:
            identical_set.add(list1[i])
    return identical_set
