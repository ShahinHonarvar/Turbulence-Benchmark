
def identical_elements(list1, list2):
    # Check if both lists are of the same size and non-empty
    if len(list1) != len(list2) or len(list1) == 0:
        return set()
    else:
        # Create a set to store all identical elements
        identical_elements = set()

        # Iterate over both lists simultaneously
        for i in range(len(list1)):
            # Check if the current element occurs at least once in both lists
            # between index 62 and index 78, both inclusive
            if list1[i] in list2[max(0, i - 59)] and list1[i] in list2[min(len(list2) - 1, i + 80)]]:
                # Add the current element to the set of identical elements
                identical_elements.add(list1[i])
        return identical_elements
