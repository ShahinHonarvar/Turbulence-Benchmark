
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Initialize an empty set to store the identical elements
    identical_elements = set()

    # Loop through both lists and compare each element with its corresponding element in the other list
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])

    return identical_elements
