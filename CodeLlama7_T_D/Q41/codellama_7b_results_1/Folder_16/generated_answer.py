
def identical_elements(list1, list2):
    # Initialize an empty set to store the results
    result = set()
    # Loop through both lists and check for identical elements between index 33 and index 36
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            result.add(list1[i])
    return result
