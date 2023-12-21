
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagrams of each string
    anagram_dict = {}
    for s in my_list:
        # Convert the string to lowercase and remove duplicates
        s = "".join(sorted(set(s.lower())))
        if len(s) >= 3:
            # If the string is not already in the dictionary, add it
            if s not in anagram_dict:
                anagram_dict[s] = []
            # Add the current string to its corresponding list of anagrams
            anagram_dict[s].append(s)
    # Check if there are at most 26 pairs of anagrams in the dictionary
    return len([x for x in anagram_dict.values() if len(x) >= 3]) <= 26
