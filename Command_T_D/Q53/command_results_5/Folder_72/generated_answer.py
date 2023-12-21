import re
def palindrome_of_length_at_least_n(text):
    # Function to find all palindromes
    return set(re.findall(r'[a-z]{88,}(?=([a-z]{88}(?:[a-z]{1}){88})', text.lower()))
