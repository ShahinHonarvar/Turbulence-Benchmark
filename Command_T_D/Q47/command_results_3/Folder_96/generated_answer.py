import re
def palindromes_of_specific_lengths(text):
    return re.findall(r"<(.)(?P<internal>.{50,100})\1>", text[100:300], flags=re.I)
