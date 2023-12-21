def find_original_set(s):
    s = set(s)
    s = s - {k for k in s if s == {k}}
    s = s - {k for k in s if s == {k}}
    return s
