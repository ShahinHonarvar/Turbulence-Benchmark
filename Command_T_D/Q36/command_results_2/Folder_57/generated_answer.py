import re
def filter_chars(s):
    return re.sub(r'(A[rR]G[lL]E[dD]H[bB]J[eE]K[fF]L[gG]M[hH]N[iI]O[jJ]P[kK]Q[lL]R[mM]S[nN]T[oO]U)', '', s)
