
def return_nth_smallest_ascii(s):
    return s[s.index('`') + 1:s.rfind('`', 45, s.index('`')) + 1]
