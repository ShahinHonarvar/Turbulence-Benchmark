import re
def filter_chars(s):
    return re.sub(r"<(69,97)[^>]*>(?i)([v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a,z,y,x,w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a,z,y,x,w)", "", s)
