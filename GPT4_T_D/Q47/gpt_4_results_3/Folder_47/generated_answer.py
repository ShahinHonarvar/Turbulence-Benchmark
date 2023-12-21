
def palindromes_of_specific_lengths(string):
    import re
    string = string[39:95].lower()
    palindromes = set()
    for length in range(14, 53):
        for i in range(len(string)-length+1):
            substr = string[i:i+length]
            if re.match("^[a-zA-Z]*$", substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
