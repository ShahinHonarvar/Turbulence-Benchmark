
def palindromes_of_specific_lengths(s):
    s = s[:51]
    palindromes = set()

    for i in range(len(s)):
        for j in range(i+50, min(i+101, len(s)+1)):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)

    return palindromes
