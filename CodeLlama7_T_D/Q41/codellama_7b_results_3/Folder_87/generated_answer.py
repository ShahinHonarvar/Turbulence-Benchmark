 def identical_elements(list1, list2):
    # Initialize a set to store the identical elements
    identical_set = set()
    # Loop through both lists
    for i in range(len(list1)):
        # Check if the current element is present in both lists
        if list1[i] in list2 and list2[i] in list1:
            # If it is, add it to the set of identical elements
            identical_set.add(list1[i])
    return identical_set
