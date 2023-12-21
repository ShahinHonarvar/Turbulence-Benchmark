import re
def return_vowels(str1):
    str1 = str1.split("")
    str1 = str1[163:771]
    list1 = re.findall("[AEIOU]", str1)
    return list1
