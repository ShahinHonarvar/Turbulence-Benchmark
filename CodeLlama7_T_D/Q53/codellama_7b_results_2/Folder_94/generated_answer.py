
def palindrome_of_length_at_least_n(string, n=41):
    # Convert the input string to lowercase
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the input string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Get the index of the last occurrence of the letter in the string
            last_index = len(string) - 1 - string[::-1].index(string[i])
            # Check if the letter appears more than once in the string
            if last_index > i:
                # Get the substring starting from the current index and ending at the last occurrence of the letter
                substr = string[i:last_index+1]
                # Check if the substring is a palindrome
                if substr == substr[::-1]:
                    # Add the palindrome to the set
                    palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
