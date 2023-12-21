def filter_chars(s):
    s = s[1:-1]
    return s.replace("d", "e").replace("h", "i").replace("j", "k").replace("l", "m").replace("o", "p").replace("q", "r").replace("s", "t").replace("v", "w").replace("x", "y").replace("z", "`")
