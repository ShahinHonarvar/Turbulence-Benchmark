
def palindromes_of_specific_lengths(string):
    import re
    string = string[:5].lower()
    palindromes = set()
    for length in range(3, 5):
        for start in range(len(string)-length+1):
            substr = string[start:start+length]
            if re.match(r'^[a-zA-Z]+$', substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
