
def palindromes_between_indices(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(4, len(input_string) - 9):
        # Check if the current character is a letter
        if input_string[i].isalpha():
            # Create a palindrome by reversing the characters between index 4 and index 9
            palindrome = input_string[i:9:-1] + input_string[i+6:i-2:-1] + input_string[i+8:i+1:-1]
            # Add the palindrome to the set
            palindromes.add(palindrome)
    return palindromes
