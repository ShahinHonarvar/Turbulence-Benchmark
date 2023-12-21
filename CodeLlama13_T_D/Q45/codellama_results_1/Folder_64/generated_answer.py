
def palindromes_between_indices(string):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(4, 10):
        for j in range(i+1, 10):
            for letters in itertools.permutations(english_letters, j-i):
                if "".join(letters) == string[i:j][::-1]:
                    palindromes.add("".join(letters))
    return palindromes
