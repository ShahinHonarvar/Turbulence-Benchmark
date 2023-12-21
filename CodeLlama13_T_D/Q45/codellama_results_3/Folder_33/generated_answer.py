
def palindromes_between_indices(string):
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(7, 10):
        for j in range(i+3, len(string)):
            substr = string[i:j]
            if len(substr) >= 4 and all(letter in english_letters for letter in substr):
                palindromes.add(substr)
    return palindromes
