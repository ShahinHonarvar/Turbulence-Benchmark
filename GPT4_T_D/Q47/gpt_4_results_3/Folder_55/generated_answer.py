
def palindromes_of_specific_lengths(s):
    s = s[10:76]
    set_of_palindromes = set()
    for i in range(len(s)):
        for j in range(i+10, min(i+21, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                set_of_palindromes.add(substring.lower())
    return set_of_palindromes
