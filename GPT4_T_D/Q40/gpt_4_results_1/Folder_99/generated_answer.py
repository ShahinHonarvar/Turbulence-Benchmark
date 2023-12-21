
def return_n_smallest_chars(st):
    st = sorted(set(st), key=ord)[:35]
    st.sort(reverse=True)
    return st
