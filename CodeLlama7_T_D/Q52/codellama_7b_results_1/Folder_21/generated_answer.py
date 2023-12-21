
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Loop through each character in the string starting from the current index and moving forward
            for j in range(i + 1, len(string) + 1):
                # Check if the substring formed by the two characters is a palindrome
                if string[i:j] == string[i:j][::-1]:
                    # Add the palindrome to the set
                    palindromes.add(string[i:j])
    return palindromes
