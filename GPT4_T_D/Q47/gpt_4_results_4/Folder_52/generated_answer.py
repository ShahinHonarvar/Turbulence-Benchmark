
import re
def palindromes_of_specific_lengths(text):
    text = text[44:100].lower()
    text = re.sub('[^a-z]', '', text)
    palindrome_set = set()
    for i in range(len(text)):
        for j in range(i+13, min(i+43, len(text)+1)):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
