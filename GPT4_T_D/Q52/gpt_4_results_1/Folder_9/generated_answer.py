
def palindrome_of_length_n(text):
    text = text.lower()
    palindrome_set = set()
    for i in range(len(text) - 71):
        substring = text[i:i+72]
        if substring == substring[::-1] and substring.isalpha():
            palindrome_set.add(substring)
    return palindrome_set
