
def palindromes_between_indices(string):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(2, 8+1):
        for j in range(i+3, len(string)+1):
            substr = string[i:j]
            if substr == substr[::-1] and all(letter in english_letters for letter in substr):
                palindromes.add(substr)
    return palindromes
