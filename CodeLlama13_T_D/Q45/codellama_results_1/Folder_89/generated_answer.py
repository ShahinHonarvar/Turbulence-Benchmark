
def palindromes_between_indices(string):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(5, 10):
        for j in range(i + 6, len(string)):
            substr = string[i:j]
            if all(letter in english_letters for letter in substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
