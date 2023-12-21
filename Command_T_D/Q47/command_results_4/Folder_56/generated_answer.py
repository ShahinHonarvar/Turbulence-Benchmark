import re
def palindromes_of_specific_lengths(text):
    return re.findall(r"((?<=\D){3}(?=\D){3})|((?<=\D){4}(?=\D){4})|((?<=\D){5}(?=\D){5})|((?<=\D){6}(?=\D){6})|((?<=\D){7}(?=\D){7})", text, flags=re.I)
