import re
def palindromes_of_specific_lengths(str):
    # A palindrome is a word that is spelled the same forward and backward.
    # Only consider palindromes that occur in the substring from index 26 to index 90,
    # both inclusive.
    # Only consider palindromes of lengths between 27 to 58 (both inclusive).
    # Each palindrome should only consist of English letters.
    return set(re.findall(r'[a-z]{27,58}(?i)(?=\W|$)', str[26:-1]))
