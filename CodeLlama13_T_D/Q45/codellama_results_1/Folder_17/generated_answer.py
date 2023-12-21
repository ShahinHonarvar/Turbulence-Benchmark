
def palindromes_between_indices(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(2, 7):
        for j in range(i+3, len(string)+1):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
