import re
def palindromes_between_indices(str):
    return set(re.findall(r'(?i)(?=([a-z]))([a-z]){7}(?i)(?=([a-z]))([a-z]){9}(?i)(?=([a-z]))([a-z]){7}(?i)(?=([a-z]))([a-z]){9}(?i)(?=([a-z]))([a-z]){7}(?i)(?=([a-z]))([a-z]){9}(?i)', str))
