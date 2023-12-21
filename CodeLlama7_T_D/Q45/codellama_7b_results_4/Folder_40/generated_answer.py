
def palindromes_between_indices(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(4, len(input_string) - 9):
        # Check if the substring starting from index 4 and ending at index 9 is a palindrome
        if input_string[i:i+9] == input_string[i:i+9][::-1]:
            # Add the palindrome to the set
            palindromes.add(input_string[i:i+9])
    return palindromes
