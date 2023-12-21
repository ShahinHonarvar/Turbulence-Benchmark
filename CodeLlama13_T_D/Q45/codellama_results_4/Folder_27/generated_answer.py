
def palindromes_between_indices(string):
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(2, 9):
        for j in range(i+1, 9):
            substr = string[i:j]
            if len(substr) < 6:
                continue
            if "".join(sorted(substr)) in english_letters and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
