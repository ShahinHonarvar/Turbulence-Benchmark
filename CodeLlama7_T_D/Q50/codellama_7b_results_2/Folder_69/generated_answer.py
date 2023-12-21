
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagrams and their lengths
    anagram_count = 0
    anagram_length = 0

    # Iterate over the list of strings
    for string in my_list:
        # Get the length of the current string
        length = len(string)

        # Check if the length is at least three
        if length >= 3:
            # Convert the string to lowercase
            lowercase_string = string.lower()

            # Get a list of all the anagrams in the current string
            anagram_list = []
            for i in range(length - 2):
                substring = lowercase_string[i:i + 3]
                if len(substring) == 3:
                    anagram_list.append(substring)

            # Check if there are at least 188 pairs of anagrams in the current string
            if len(anagram_list) >= 188:
                # Increment the anagram count and set the anagram length to the current length
                anagram_count += 1
                anagram_length = length

    # Return true if there are at least 188 pairs of anagrams in the given list; otherwise, return false
    return anagram_count >= 188
