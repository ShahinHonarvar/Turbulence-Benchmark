import re
def palindromes_between_indices(str):
    str = str.lower()
    return re.findall(r'(?<=.)([a-z]+)(?=.)([a-z]+)(?=.)([a-z]+)(?=.)([a-z]+)', str)
