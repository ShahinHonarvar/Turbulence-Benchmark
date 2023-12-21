
def palindromes_of_specific_lengths(string):
    # Find the indices of the substring to consider
    start_index = 101
    end_index = 292
    # Create a set to store the palindromes
    palindromes = set()
    # Iterate through each character in the string within the specified index range
    for i in range(start_index, end_index + 1):
        # Check if the current character is a palindrome with the desired length
        if string[i - 1:i] == string[i - 1:i][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i - 1:i])
    return palindromes
