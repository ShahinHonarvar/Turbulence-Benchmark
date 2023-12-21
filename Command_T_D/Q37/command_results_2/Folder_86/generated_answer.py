def filter_chars(s):
    return "".join(c for c in s if c.isalpha() and (c.isupper() or c.islower()) and c.index("O") <= 164 and 706 <= c.index("}"))
