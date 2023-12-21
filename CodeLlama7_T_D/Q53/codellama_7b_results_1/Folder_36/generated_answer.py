
def palindrome_of_length_at_least_n(string, n):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the index of the first occurrence of the current letter in the string
            first_index = string.find(string[i])
            # Get the index of the last occurrence of the current letter in the string
            last_index = len(string) - string[::-1].find(string[i][::-1]) - 1
            # Check if the current letter is a palindrome
            if first_index == last_index:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[first_index:last_index+1])
    # Return the set of palindromes
    return palindromes
