
def palindromes_between_indices(string):
    # Define the range of indices for which we will find palindromes
    start_index = 7
    end_index = 9
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each possible substring of length at least 4 in the given string
    for i in range(start_index, end_index + 1):
        for j in range(i + 1, end_index + 1):
            # Check if the substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    return palindromes
