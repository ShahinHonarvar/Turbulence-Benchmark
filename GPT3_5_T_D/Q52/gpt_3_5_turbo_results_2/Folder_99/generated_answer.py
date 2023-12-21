
def palindrome_of_length_n(string: str) -> set:
    palindromes = set()
    n = 420
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if substr.lower() == substr.lower()[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes
