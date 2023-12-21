
def identical_elements(list1, list2):
    # Create an empty set to store the results
    results = set()

    # Iterate over both lists simultaneously and check for identical elements
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                results.add(list1[i])

    return results
