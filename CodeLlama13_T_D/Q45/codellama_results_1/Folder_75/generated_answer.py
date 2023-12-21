
def palindromes_between_indices(s):
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(2, 5):
        for j in range(i+1, len(s)):
            substr = s[i:j]
            if all(letter in english_letters for letter in substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
