
def palindromes_of_specific_lengths(string, min_len=38, max_len=49):
    # Convert the input string to lowercase for case-insensitive matching
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over the characters in the substring from index 28 to index 94, both inclusive

    for i in range(28, 95):
        # Get the length of the current substring

        len_sub = i - 27

        # Check if the current substring is within the specified range of lengths

        if min_len <= len_sub <= max_len:
            # Initialize an empty string to store the palindrome

            palindrome = ""

            # Iterate over the characters in the current substring, starting from the middle character and moving outwards

            for j in range(i - int(len_sub / 2), i + int((len_sub + 1) / 2)):
                # Add the current character to the palindrome string

                palindrome += string[j]

            # Check if the constructed palindrome is a valid English word

            if palindrome in english_words:
                # If it is, add it to the set of palindromes

                palindromes.add(palindrome)

    return palindromes
