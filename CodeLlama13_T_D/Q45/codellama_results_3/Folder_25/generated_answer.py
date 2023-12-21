
def palindromes_between_indices(s):
    letters = set("aebdfhilmnorstu")
    palindromes = set()
    for i in range(1, 4+1):
        for j in range(len(s)-i+1):
            substr = s[j:j+i]
            if len(substr) < 3:
                continue
            if all(letter in letters for letter in substr):
                palindromes.add(substr)
    return palindromes
