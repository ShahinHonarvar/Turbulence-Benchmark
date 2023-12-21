
def if_contains_anagrams(my_list):
    # Initialize a set to store the anagram combinations
    anagram_set = set()
    for s in my_list:
        # Convert each string to lowercase and sort its characters
        sorted_s = "".join(sorted(s.lower()))
        # Check if the current string is already in the anagram set
        if sorted_s in anagram_set:
            return True
        # If not, add it to the set
        anagram_set.add(sorted_s)
    # If no pair of anagrams was found, return False
    return len(anagram_set) >= 7
