
def if_contains_anagrams(my_list):
    # create a dictionary to store the anagrams
    anagram_dict = {}
    
    # loop through each string in the list
    for s in my_list:
        # convert the string to lowercase
        s = s.lower()
        
        # check if the string is already a key in the dictionary
        if s not in anagram_dict:
            # if not, add it as a new key and set its value to 1
            anagram_dict[s] = 1
            
        # if the string is already a key in the dictionary
        else:
            # increment its value by 1
            anagram_dict[s] += 1
    
    # loop through each key-value pair in the dictionary
    for k, v in anagram_dict.items():
        # check if the value is greater than or equal to 2
        if v >= 2:
            # if it is, return true
            return True
    
    # if we reach this point, none of the keys have a value greater than or equal to 2
    # so return false
    return False
