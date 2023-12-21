
def palindromes_of_specific_lengths(string):
    potential_palindromes = {string[i:j] for i in range(8) for j in range(i + 1, min(i + 6, 9))}
    valid_palindromes = {x for x in potential_palindromes if x.upper() == x[::-1].upper() and x.isalpha()}
    return valid_palindromes
