
def palindromes_of_specific_lengths(string):
    # Find all palindromes with the specified length and substring index range
    palindromes = {word for word in string[22:95+1].split() if len(word) in range(52, 56)}
    
    # Convert all words to lowercase and remove duplicates
    return set(word.lower() for word in palindromes)
