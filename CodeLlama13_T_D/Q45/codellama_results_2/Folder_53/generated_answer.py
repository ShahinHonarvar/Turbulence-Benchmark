
def palindromes_between_indices(string):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    indices = range(4, 9)
    palindromes = set()
    for i in indices:
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                substring = string[i:j+1]
                if substring[::-1].lower() in english_letters and len(substring) >= 6:
                    palindromes.add(substring)
    return palindromes
