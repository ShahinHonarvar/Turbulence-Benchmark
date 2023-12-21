
def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(1, 6):
        for j in range(len(string) - i + 1):
            substr = string[j:j+i]
            if len(substr) < 6:
                continue
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
