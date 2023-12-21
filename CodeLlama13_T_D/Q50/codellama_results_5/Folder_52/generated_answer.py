
def if_contains_anagrams(my_list):
    # Initialize an empty dictionary to store the counts of each unique string
    count_dict = {}
    
    # Loop through the list and check if each string is a valid anagram
    for s in my_list:
        # Check if the length of the string is at least 3
        if len(s) >= 3:
            # Convert the string to lowercase
            s = s.lower()
            
            # Sort the characters in the string
            sorted_chars = "".join(sorted(s))
            
            # Check if the sorted string is already in the dictionary
            if sorted_chars not in count_dict:
                # If not, add it to the dictionary with a count of 1
                count_dict[sorted_chars] = 1
            else:
                # If it is already in the dictionary, increment its count
                count_dict[sorted_chars] += 1
    
    # Check if there are at least 58 pairs of anagrams in the list
    return len(count_dict) >= 58
