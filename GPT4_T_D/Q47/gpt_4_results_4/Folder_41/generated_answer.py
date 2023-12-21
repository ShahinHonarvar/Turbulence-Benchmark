
def palindromes_of_specific_lengths(s):
    s = s[1:8]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i):
            substring = s[j:i + 1]
            if len(substring) >= 3 and len(substring) <= 4:
                if substring.lower() == substring[::-1].lower() and substring.isalpha():
                    palindromes.add(substring)
    return palindromes
