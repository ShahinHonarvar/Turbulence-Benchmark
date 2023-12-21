
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a digit or a symbol)
        if string[i].isalpha():
            # Get the substring starting from the current index and ending at the length of the string minus 1
            substr = string[i:len(string)-1]
            # Loop through each character in the substring in reverse order
            for j in range(len(substr)-1, -1, -1):
                # Check if the current character is the same as the previous character
                if substr[j] == substr[j-1]:
                    # If the current character is the same as the previous character, add the substring to the set of palindromes
                    palindromes.add(substr)
                    # Break out of the inner loop and continue with the outer loop
                    break

    # Return the set of palindromes found in the string
    return palindromes
