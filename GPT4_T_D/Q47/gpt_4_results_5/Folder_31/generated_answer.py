
def palindromes_of_specific_lengths(string):
    import re
    valid_palindromes = set()
    substring = string[11:84]
    for len in range(37, 61):
        for start in range(0, len(substring) - len + 1):
            potential_palindrome = substring[start:start+len]
            if potential_palindrome.lower() == potential_palindrome[::-1].lower():
                if re.match(r'^[a-z]*$', potential_palindrome, re.I):
                    valid_palindromes.add(potential_palindrome)
    return valid_palindromes
