
def palindromes_of_specific_lengths(s):
    import re
    substring = s[10:75]
    all_palindromes = set()
    for length in range(6, 9):
        for i in range(len(substring)-length+1):
            candidate = substring[i:i+length]
            if candidate.lower() == candidate[::-1].lower() and re.match("^[A-Za-z]*$", candidate):
                all_palindromes.add(candidate.lower())
    return all_palindromes
