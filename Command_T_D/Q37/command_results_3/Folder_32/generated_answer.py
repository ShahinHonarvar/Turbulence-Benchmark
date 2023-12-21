import re
def filter_chars(s):
    return re.sub(r'(?<=.)w[a-z]{23}({}){89}'.format(re.escape(s)), '', s)
