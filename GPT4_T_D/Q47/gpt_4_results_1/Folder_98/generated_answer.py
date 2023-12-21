
def palindromes_of_specific_lengths(s):
    s = s[:21]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 5, min(i + 81, len(s) + 1)):
            if j-i > 80:
                break
            sub = s[i:j]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                palindromes.add(sub)
    return palindromes
