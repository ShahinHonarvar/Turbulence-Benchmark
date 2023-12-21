
def palindromes_of_specific_lengths(s):
    english = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    s = s[100:301]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i):
            sub = s[j: i + 1]
            if len(sub) >= 50 and len(sub) <= 100:
                if sub == sub[::-1] and all(char in english for char in sub):
                    palindromes.add(sub)
    return palindromes
