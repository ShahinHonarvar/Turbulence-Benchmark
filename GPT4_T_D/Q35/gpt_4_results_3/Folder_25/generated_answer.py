
def remove_repeat_chars(st):
    subset = st[38:43]
    for char in subset:
        if subset.count(char) > 1:
            st = st.replace(char, '') 
    return st
