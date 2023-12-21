
def palindromes_of_specific_lengths(string):
    # find all palindromes in the string with case-insensitive comparison
    palindromes = {substring for substring in string.lower() if substring == substring[::-1]}
    
    # filter palindromes to only those that occur within index 23 to 82, both inclusive
    filtered_palindromes = {substring for substring in palindromes if len(substring) >= 32 and len(substring) <= 34}
    
    # return the set of all palindromes with the required length
    return filtered_palindromes
