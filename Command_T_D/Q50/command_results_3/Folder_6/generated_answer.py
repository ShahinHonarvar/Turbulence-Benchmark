import re
def if_contains_anagrams(input_str):
    res = True
    for i in input_str:
        for j in input_str:
            if re.fullmatch(i, j, re.IGNORECASE):
                if i != j:
                    res = False
                    break
    return res
