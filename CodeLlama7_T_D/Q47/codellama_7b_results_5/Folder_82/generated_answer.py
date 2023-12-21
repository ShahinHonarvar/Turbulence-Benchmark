
def palindromes_of_specific_lengths(string):
    # Define the range of lengths for the palindromes
    length_range = range(30, 301)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(3, 301):
        # Check if the substring from index 3 to index 300 is a palindrome
        if string[i:i+length_range] == string[i:i+length_range][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+length_range])
    return palindromes
