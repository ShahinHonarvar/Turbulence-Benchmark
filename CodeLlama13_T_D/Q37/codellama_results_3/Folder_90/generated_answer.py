
def filter_chars(string):
    for i in range(348, 852+1):
        if string[i].lower() >= "j" and string[i].lower() <= "b":
            string = string[:i] + string[i+1:]
    return string
