
def palindrome_of_length_at_least_n(string, n):
    # Convert the string to lowercase
    string = string.lower()
    
    # Find all palindromes in the string that are at least 67 characters long
    palindromes = [word for word in string.split() if len(word) >= 67 and word == word[::-1]]
    
    # Return the set of unique palindromes
    return set(palindromes)
