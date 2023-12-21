 def palindrome_of_length_at_least_n(string, n):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # Check if the character is a letter
        if char.isalpha():
            # Convert the character to lowercase
            lowercase_char = char.lower()
            # Reverse the string from index i to the end
            reversed_substring = string[i:].lower()[::-1]
            # Check if the reverse of the substring is a palindrome
            if lowercase_char + reversed_substring == lowercase_char * 2:
                # If it is, add it to the set of palindromes
                palindromes.add(lowercase_char + reversed_substring)
    # Return the set of palindromes
    return palindromes
