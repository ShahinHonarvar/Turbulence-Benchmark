
def palindromes_between_indices(string):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(2, 6):
        for j in range(i+4, len(string)):
            if string[i:j] == string[j-1:-1]:
                palindromes.add(string[i:j])
    return palindromes
