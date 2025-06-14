
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the substring starting from the current character and ending at the end of the string
            substr = string[i:].lower()
            # Loop through each word in the substring
            for j in range(len(substr.split())):
                # Check if the current word is a palindrome
                if substr.split()[j] == substr.split()[j][::-1]:
                    # If the current word is a palindrome, add it to the set of palindromes
                    palindromes.add(substr.split()[j])
    # Return the set of palindromes
    return palindromes
