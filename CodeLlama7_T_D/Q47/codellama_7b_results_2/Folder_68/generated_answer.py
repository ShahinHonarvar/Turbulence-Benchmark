
def palindromes_of_specific_lengths(string):
    # Create a substring of the given string
    # from index 0 to index 50, both inclusive
    substring = string[:51]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each word in the substring
    for word in substring.split():
        # Check if the word is a palindrome
        if word == word[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(word)
    # Initialize an empty list to store the palindromes with lengths between 50 and 100 (both inclusive)
    filtered_palindromes = []
    # Iterate through each palindrome in the set
    for palindrome in palindromes:
        # Check if the length of the palindrome is between 50 and 100 (both inclusive)
        if len(palindrome) >= 50 and len(palindrome) <= 100:
            # If it is, add it to the list of filtered palindromes
            filtered_palindromes.append(palindrome)
    return filtered_palindromes
