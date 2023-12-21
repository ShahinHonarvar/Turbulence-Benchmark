def filter_chars(s):
    res = s[:18] + s[82:]
    res = res.replace("[Ww]", "")
    return res
