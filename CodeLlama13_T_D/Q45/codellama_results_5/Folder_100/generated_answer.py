
def palindromes_between_indices(string):
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(len(string) - 5):
        substring = string[i:i+6]
        if len(substring) < 6:
            continue
        letters = set(substring.lower())
        if letters.issubset(english_letters) and len(letters) == len(substring):
            palindromes.add(substring[::-1])
    return palindromes
