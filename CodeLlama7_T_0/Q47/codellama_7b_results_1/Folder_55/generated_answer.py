
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    start = 10
    end = 75
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start, end + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the left and right indices for the palindrome
            left = i - (len(string) - end)
            right = i + (end - start)
            # Check if the palindrome is of the specified length
            if len(string[left:right]) == 10 or len(string[left:right]) == 20:
                # Add the palindrome to the set
                palindromes.add(string[left:right])
    return palindromes
