import re
def palindromes_between_indices(s):
    reg = r'(?i)(?=([a-z])[a-z]{4}([a-z]))([a-z]{4})([a-z]?)\1([a-z]?)\2([a-z]{4})\3([a-z]?)\4([a-z]?)\5([a-z]?)\6([a-z]?)\7([a-z]?)\8([a-z]?)\9([a-z]?)'
    return re.findall(reg, s, flags=re.I)
