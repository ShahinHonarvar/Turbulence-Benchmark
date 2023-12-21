 
import re
def palindromes_of_specific_lengths(s):
    pat = re.compile(r"([a-z]+)(?=([a-z][a-z]{13}){2})")
    return {m[0].lower() for m in pat.finditer(s, flags=re.I)}
