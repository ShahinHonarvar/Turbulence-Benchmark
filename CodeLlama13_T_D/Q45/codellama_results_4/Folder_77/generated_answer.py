
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(4, 7):
        for j in range(i + 1, len(string)):
            if string[i:j].lower() == string[i:j][::-1].lower():
                palindromes.add(string[i:j])
    return palindromes
