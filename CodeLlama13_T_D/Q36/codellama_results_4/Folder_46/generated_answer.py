
def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if (i >= 19 and i < 69) and char > "<" and char < "C":
            continue
        result.append(char)
    return "".join(result)
