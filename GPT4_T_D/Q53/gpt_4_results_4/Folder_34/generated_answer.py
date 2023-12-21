
def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i+68, len(text)+1):
            substr = text[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
