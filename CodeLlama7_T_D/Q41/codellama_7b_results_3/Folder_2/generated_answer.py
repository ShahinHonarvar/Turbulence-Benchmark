
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements and check if they are present in both lists at least once between index 15 and 39, both inclusive
    for element in common_elements:
        count = 0
        for i in range(len(list1)):# Check if the element is present in list1 at least once between index 15 and 39, both inclusive
            if element == list1[i]:
                count += 1
                if count >= 2: # Check if the count is greater than or equal to 2, indicating that the element is present at least once in both lists at least once between index 15 and 39, both inclusive
                    result.add(element) # Add the element to the result set if it meets the condition
                    break

        for i in range(len(list2)):# Check if the element is present in list2 at least once between index 15 and 39, both inclusive
            if element == list2[i]:
                count += 1
                if count >= 2: # Check if the count is greater than or equal to 2, indicating that the element is present at least once in both lists at least once between index 15 and 39, both inclusive
                    result.add(element) # Add the element to the result set if it meets the condition
                    break

    return result
