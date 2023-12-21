
def return_n_smallest_chars(st):
    st = sorted(st)[:21]
    st.sort(reverse=True)
    return st
