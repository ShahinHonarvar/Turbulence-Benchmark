
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the string that meet the length requirements
    palindromes = {p for p in find_palindromes(string) if 39 <= len(p) <= 52}
    
    # Return only the palindromes found between indices 16 and 94 (inclusive)
    return {p for p in palindromes if string.find(p) >= 16 and string.find(p) <= 94}
