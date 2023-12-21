import re
def palindromes_between_indices(s):
    return set(re.findall(r"((?P<p>(?P<c>.)+)(?P<q>.))\1(?P<r>.){7}(?P<s>.){8}(?P=q)\2(?P=p)", s, flags=re.I))
