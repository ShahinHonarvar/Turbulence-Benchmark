
def identical_elements(list1, list2):
    # Check if both lists have at least one element
    if len(list1) == 0 or len(list2) == 0:
        return set()
    # Find the first index where elements are not identical
    first_non_identical_index = 0
    while first_non_identical_index < len(list1) and first_non_identical_index < len(list2):
        if list1[first_non_identical_index] != list2[first_non_identical_index]:
            break

        first_non_identical_index += 1

    # Find the last index where elements are not identical
    last_non_identical_index = len(list1) - 1
    while last_non_identical_index >= 0 and last_non_identical_index >= first_non_identical_index:
        if list1[last_non_identical_index] != list2[last_non_identical_index]:
            break

        last_non_identical_index -= 1

    # Find the set of identical elements between the two lists
    identical_elements = set()

    for i in range(first_non_identical_index, last_non_identical_index + 1):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])

    return identical_elements
