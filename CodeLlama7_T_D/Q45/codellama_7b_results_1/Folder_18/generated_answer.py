
def palindromes_between_indices(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of the input string
    for i in range(len(input_string) - 2):
        # Check if the substring is a palindrome
        if input_string[i:i+3] == input_string[i:i+3][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(input_string[i:i+3])
    return palindromes
