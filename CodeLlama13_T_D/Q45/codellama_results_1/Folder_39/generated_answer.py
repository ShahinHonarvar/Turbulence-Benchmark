
def palindromes_between_indices(s):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    indices = range(2, 6)
    palindromes = []
    for i in indices:
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                substring = s[i:j+1]
                if all([letter in substring for letter in letters]) and substring not in palindromes:
                    palindromes.append(substring)
    return set(palindromes)
