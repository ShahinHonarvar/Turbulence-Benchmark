
def palindromes_between_indices(string):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(0, len(string) - 3):
        for j in range(i + 1, len(string) - 2):
            if string[i] == string[j]:
                substring = string[i:j + 1]
                if len(substring) >= 4 and all(letter in letters for letter in substring.lower()):
                    palindromes.add(substring)
    return palindromes
