 
import re
def palindromes_of_specific_lengths(text):
    patterns = ["{:<=12}|{:>92}"]
    for i in range(42, 77):
        patterns.append("{{:{}{{}}:{}{{}}".format(i, i))
    return set(re.findall(r"{}".format("|".join(patterns)), text.lower()))
