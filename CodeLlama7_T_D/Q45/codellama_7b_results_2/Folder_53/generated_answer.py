
def palindromes_between_indices(string):
    # Create a list of all English letters in the given string
    letter_list = [char for char in string if char.isalpha()]
    # Create a set to store all palindromes of length at least 6
    palindrome_set = set()
    # Iterate through each possible arrangement of the English letters in the given string that occur between index 4 to index 8, both inclusive
    for i in range(4, len(letter_list) - 2):
        # Check if the current letter is a palindrome
        if letter_list[i] == letter_list[i]:
            # Create a substring of length at least 6 from the English letters of the given string that occur between index 4 to index 8, both inclusive
            substring = "".join(letter_list[i:i + 6])
            # Check if the current substring is a palindrome in a case-insensitive manner
            if substring.lower() == substring[::-1].lower():
                # Add the current palindrome to the set of all palindromes
                palindrome_set.add(substring)
    # Return the set of all palindromes of length at least 6 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 4 to index 8, both inclusive
    return palindrome_set
