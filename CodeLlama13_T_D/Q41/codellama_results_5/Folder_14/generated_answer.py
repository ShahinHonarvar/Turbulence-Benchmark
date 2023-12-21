
def identical_elements(list1, list2):
    # Set to store the common elements between both lists
    common_elements = set()
    
    # Iterate through each element in list1 and check if it is also present in list2
    for i in range(5, 8):
        if list1[i] in list2:
            common_elements.add(list1[i])
            
    return common_elements
