
def palindrome_of_length_at_least_n(word):
    word = word.lower()
    palindromes = set()
    for i in range(len(word)):
        for j in range(i+38, len(word)+1):
            if word[i:j] == word[i:j][::-1]:
                palindromes.add(word[i:j])
    return palindromes
