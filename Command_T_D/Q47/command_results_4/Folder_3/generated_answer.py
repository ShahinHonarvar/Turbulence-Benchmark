import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?P<a>.{49,50})(?P<b>.{49,50})\1(?P<c>.{49,50})\2(?P<d>.{49,50})\3(?P<e>.{49,50})\4(?P=a)\5(?P=b)\6(?P=c)\7(?P=d)\8(?P=e)\9(?P=a)\10(?P=b)\11(?P=c)\12(?P=d)\13(?P=e)\14(?P=a)\15(?P=b)\16(?P=c)\17(?P=d)\18(?P=e)', s[27:95]))
