
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the substring from index 200 to index 300, both inclusive
    for i in range(200, 300 + 1):
        # Check if the substring is a palindrome
        if string[i:i+1] == string[i:i+1][::-1]:
            # If it's a palindrome, check its length and add it to the set if it falls within the specified range
            if 10 <= len(string[i:i+1]) <= 50:
                palindromes.add(string[i:i+1])

    # Return the set of all palindromes with the required length and index range
    return palindromes
