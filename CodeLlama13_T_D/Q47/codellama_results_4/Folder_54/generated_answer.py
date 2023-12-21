
def palindromes_of_specific_lengths(string):
    # Get the substring from index 27 to index 77, both inclusive
    substr = string[27:78]
    
    # Create a set of all palindromes with lengths between 18 and 19
    palindromes = {p for p in substr.split() if len(p) in range(18, 20)}
    
    # Return the set of all palindromes that are English letters only
    return {p for p in palindromes if all(c.isalpha() and c.lower() == c.upper() for c in p)}
