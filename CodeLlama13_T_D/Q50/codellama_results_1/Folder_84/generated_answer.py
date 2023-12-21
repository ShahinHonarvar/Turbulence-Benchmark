
def if_contains_anagrams(my_list):
    # initialize a dictionary to store anagram counts
    anagram_counts = {}
    # iterate over the list of strings
    for s in my_list:
        # convert the string to lowercase
        s = s.lower()
        # sort the characters in the string
        sorted_chars = "".join(sorted(s))
        # check if the sorted string is already in the dictionary
        if sorted_chars not in anagram_counts:
            # if not, add it to the dictionary with count 1
            anagram_counts[sorted_chars] = 1
        else:
            # if yes, increment its count by 1
            anagram_counts[sorted_chars] += 1
    # iterate over the keys of the dictionary
    for k in anagram_counts.keys():
        # check if the count is at least 108
        if anagram_counts[k] >= 108:
            # if yes, return true
            return True
    # if no key has a count of at least 108, return false
    return False
