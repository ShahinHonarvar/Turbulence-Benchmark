
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Check if the character is uppercase
            if string[i].isupper():
                # Convert the character to lowercase
                string[i] = string[i].lower()
            # Get the length of the substring starting from the current index and ending at the end of the string
            substring_length = len(string) - i
            # Loop through each possible palindrome of the substring
            for j in range(substring_length):
                # Check if the substring is a palindrome
                if string[i + j] == string[i + j].lower():
                    # Add the palindrome to the set
                    palindromes.add(string[i + j])
    return palindromes
