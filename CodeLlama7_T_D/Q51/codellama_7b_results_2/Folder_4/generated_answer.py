
def if_contains_anagrams(my_list):
    # Create a set of all possible anagrams of the English letters
    all_anagrams = ["abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz"]
    # Initialize a counter for the number of anagrams in the list
    num_anagrams = 0
    # Iterate over the list and check if each string is an anagram of at least three letters
    for word in my_list:
        # Convert the word to lowercase
        lowercase_word = word.lower()
        # Check if the word is a valid anagram
        if len(lowercase_word) >= 3 and lowercase_word in all_anagrams:
            # Increment the counter for the number of anagrams in the list
            num_anagrams += 1
    # Return True if there are at most 84 pairs of anagrams in the given list, otherwise return False
    return num_anagrams <= 84
