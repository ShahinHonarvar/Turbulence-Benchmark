
def palindromes_between_indices(string):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(0, 8):
        for j in range(i + 6, 9):
            substring = string[i:j]
            if len(substring) < 6:
                continue
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
