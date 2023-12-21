
def filter_chars(string):
    return string[:71] + string[71:97].replace("_", "").replace("`", "").replace("a", "").replace("b", "").replace("c", "").replace("d", "").replace("e", "").replace("f", "").replace("g", "").replace("h", "").replace("i", "").replace("j", "").replace("k", "").replace("l", "").replace("m", "").replace("n", "").replace("o", "") + string[97:]
