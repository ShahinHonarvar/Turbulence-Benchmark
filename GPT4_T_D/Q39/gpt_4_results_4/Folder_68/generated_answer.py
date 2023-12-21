
def return_n_greatest_chars(str):
    assert len(set(str)) == len(str), "Characters in the string are not distinct."
    if len(str) >= 89:
        return sorted(str, key=lambda x: ord(x), reverse=True)[:89]
    else:
        return "The input string should have at least 89 distinct characters."
