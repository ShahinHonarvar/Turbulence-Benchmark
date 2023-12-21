import re
def if_contains_anagrams(texts):
    return bool(re.findall(r"((?i)(?<=.)(.)(?!\1)(?=.)(?!\2).+)(?i)(?<=.)(.)(?!\3)(?=.)(?!\4).+)", texts))
