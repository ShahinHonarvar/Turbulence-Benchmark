
def palindromes_between_indices(string):
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(4, 10):
        for j in range(i+6, len(string)):
            substring = string[i:j]
            if all(letter in english_letters for letter in substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
