
def palindromes_between_indices(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(3, 7):
        for j in range(i + 1, len(string)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
