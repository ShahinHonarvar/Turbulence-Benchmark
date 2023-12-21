
def filter_chars(string):
    for char in string[171:195]:
        if "!" < char < "}":
            string = string.replace(char, "")
    return string
