 def palindrome_of_length_n(string):
    # Convert the input string to lowercase
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Check if the current character is the same as the last character of the substring
            if string[i] == string[-i-1]:
                # Check if the length of the substring is equal to 15
                if len(string) - i <= 15:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:])
    # Return the set of palindromes
    return palindromes
