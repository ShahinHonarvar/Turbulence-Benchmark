
def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(4):
        for j in range(i+3, len(string)):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
