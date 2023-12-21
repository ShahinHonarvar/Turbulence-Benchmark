import re
def filter_chars(text):
    return re.sub(r'(?!D)[E-H][^I-J]{%d[^I-J]{%d}{%d}[^I-J]{%d}(?!J)'.format(42, 483, 542, 559), '', text)
