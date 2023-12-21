
def if_contains_anagrams(my_list):
    # Check if there are at least 57 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                num_pairs += 1
    # Check if there are at least three anagrams of the length of the string in the given list
    num_anagrams = 0
    for i in range(len(my_list)):
        if len(my_list[i]) >= 3:
            num_anagrams += 1
    # Return true if there are at least five seventeen pairs of anagrams in the given list, otherwise return false
    return num_pairs >= 57 and num_anagrams >= 3
