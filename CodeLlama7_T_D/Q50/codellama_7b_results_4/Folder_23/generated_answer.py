
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_letter_anagrams = []

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is an anagram of at least length three
        if len(lowercase_string) >= 3 and sorted(lowercase_string) == sorted(''.join(set(lowercase_string))[i] for i in range(len(lowercase_string)))):
            # If it is, add it to the list of three letter anagrams
            three_letter_anagrams.append(string)

        # Check if there are at least 67 pairs of anagrams in the list
        if len(three_letter_anagrams) >= 67:
            # If there are, return True
            return True

    # If there are not at least 67 pairs of anagrams in the list, return False
    return False
