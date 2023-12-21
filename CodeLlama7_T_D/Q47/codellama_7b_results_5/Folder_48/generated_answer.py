
def palindromes_of_specific_lengths(string, lengths=(104, 120)):
    # Find the index range where the palindromes occur
    start_index = 155
    end_index = 283
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(start_index, end_index + 1):
        # Check if the current character is a palindrome
        if string[i - 1] == string[i - 1:i + 1][::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[i - 1:i + 1])
    return palindromes
