
def palindromes_of_specific_lengths(string):
    # Create a substring of the given string from index 0 to index 100
    substring = string[0:100]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Check if the current character is a letter
        if substring[i].isalpha():
            # Get the length of the current word
            word_length = len(substring[i:])
            # Check if the length of the word is within the specified range
            if 3 <= word_length <= 15:
                # Convert the word to lowercase for case-insensitive comparison
                lowercase_word = substring[i:].lower()
                # Check if the word is a palindrome
                if lowercase_word == lowercase_word[::-1]:
                    # Add the word to the set of palindromes
                    palindromes.add(substring[i:])
    return palindromes
