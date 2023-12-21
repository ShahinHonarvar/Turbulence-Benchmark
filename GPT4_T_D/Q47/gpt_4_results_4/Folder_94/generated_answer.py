
def palindromes_of_specific_lengths(s):
    s = s[40:95]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start+45, min(start+52, len(s)+1)):
            substring = s[start:end]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes
