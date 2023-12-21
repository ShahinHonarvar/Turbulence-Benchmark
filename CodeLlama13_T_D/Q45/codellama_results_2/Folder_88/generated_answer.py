
def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(3, 8):
        for j in range(i + 1, len(string) - i):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(''.join(sorted(string[i:j], reverse=True)))
    return palindromes
