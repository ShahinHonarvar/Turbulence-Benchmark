import re
def filter_chars(s):
    return re.sub(r'(?<=\s[DOU]a)([DOU]b[DOU]c[DOU]d[DOU]e[DOU]f[DOU]g[DOU]h[DOU]i[DOU]j[DOU]k[DOU]l[DOU]m[DOU]n[DOU]o[DOU]p[DOU]q[DOU]r[DOU]s[DOU]t[DOU]u)', '', s)
