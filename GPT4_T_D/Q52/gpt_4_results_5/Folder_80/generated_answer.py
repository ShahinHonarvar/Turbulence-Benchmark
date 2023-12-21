
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 275):
        candidate = string[i:i+276]
        if candidate == candidate[::-1] and candidate.isalpha():
            palindromes.add(candidate)
    return palindromes
