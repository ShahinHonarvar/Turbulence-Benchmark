
def filter_chars(mstr):
    for char in mstr[47:91]:
        if 'D' < char < 'H':
            mstr = mstr.replace(char, '')
    return mstr
