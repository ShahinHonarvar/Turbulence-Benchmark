
def palindromes_of_specific_lengths(string):
    # Convert the string to lowercase for case-insensitive comparison
    lowercase_string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through the substring from index 17 to index 95, both inclusive
    for i in range(17, 96):
        # Check if the substring starting at index i is a palindrome of length between 13 and 49 (both inclusive)
        if lowercase_string[i:i+26] == lowercase_string[i:i+26][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(lowercase_string[i:i+26])
    # Return the set of palindromes found in the specified index range
    return palindromes
