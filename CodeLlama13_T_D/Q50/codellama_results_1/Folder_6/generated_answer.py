
def if_contains_anagrams(my_list):
    # Initialize a dictionary to keep track of anagrams
    anagram_dict = {}
    
    # Iterate over the list of strings and check if each string is an anagram of another string in the list
    for i, str1 in enumerate(my_list):
        for j, str2 in enumerate(my_list[i+1:]):
            if len(str1) >= 3 and len(str2) >= 3:
                if sorted(str1.lower()) == sorted(str2.lower()):
                    # If the anagrams are found, add them to the dictionary with a key of the smaller string
                    if str1 in anagram_dict or str2 in anagram_dict:
                        return True
                    else:
                        anagram_dict[str1] = 0
    
    # If no anagrams are found, return False
    return False
