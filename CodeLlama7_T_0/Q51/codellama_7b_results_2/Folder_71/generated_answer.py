
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_letters = False
    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()
        # Check if the string is an anagram of at least three letters
        if len(lowercase_string) >= 3:
            three_or_more_letters = True
        # Check if the string is a palindrome
        if lowercase_string == lowercase_string[::-1]:
            # Increment the anagram count if the string is not a palindrome
            if not lowercase_string.islower():
                anagram_count += 1

    # Return True if there are at most 9 pairs of anagrams in the given list, and False otherwise
    return anagram_count <= 9 and three_or_more_letters
