
def palindromes_of_specific_lengths(s):
    s = s[10:101].lower()
    valid_palindromes = set()
    for i in range(len(s)):
        for j in range(i+10, min(i+51, len(s)+1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                 valid_palindromes.add(substring)
    return valid_palindromes
