
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the list
    for s in my_list:
        # Convert the string to lowercase
        s = s.lower()

        # Check if the string is an anagram of an English word
        if s == ''.join(sorted(s)):
            # If it is, add 1 to the corresponding anagram count in the dictionary
            anagram_counts[s] = anagram_counts.get(s, 0) + 1

    # Check if there are at most 19 pairs of anagrams in the list
    return len(anagram_counts) <= 19
