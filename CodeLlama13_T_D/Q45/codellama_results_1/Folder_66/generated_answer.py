
def palindromes_between_indices(string):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(0, len(string) - 5 + 1):
        substring = string[i:i+6]
        if substring.lower() == substring[::-1]:
            palindromes.add(substring)
    return palindromes
