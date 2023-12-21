
def palindromes_between_indices(string):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(0, 8):
        for j in range(i + 4, 8):
            substr = string[i:j]
            if len(substr) < 4:
                continue
            rev_substr = "".join(reversed(substr))
            if substr == rev_substr and all(letter in letters for letter in substr):
                palindromes.add(substr)
    return palindromes
