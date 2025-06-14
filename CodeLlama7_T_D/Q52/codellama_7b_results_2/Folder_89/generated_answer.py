
def palindrome_of_length_n(string):
    # Split the string into a list of characters
    char_list = list(string)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(len(char_list)):
        # Get the character at index i
        char = char_list[i]
        # If the character is not a letter, continue to the next iteration
        if not char.isalpha():
            continue

        # Create a substring of length n starting from index i
        substr = "".join(char_list[i:i+n])
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    return palindromes
