
def palindromes_between_indices(string):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(1, 9):
        for j in range(i + 6, len(string)):
            if string[i:j] in english_letters and string[i:j][::-1] == string[i:j]:
                palindromes.add(string[i:j])
    return palindromes
