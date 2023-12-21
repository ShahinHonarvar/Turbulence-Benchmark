
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Loop through each character in the remainder of the string
            for j in range(i + 1, len(string) + 1):
                # Check if the substring starting at index i and ending at index j is a palindrome
                if string[i:j].lower() == string[i:j][::-1].lower():
                    # If it is, add it to the set of palindromes
                    palindromes.add(string[i:j])
    # Return the set of palindromes
    return palindromes
