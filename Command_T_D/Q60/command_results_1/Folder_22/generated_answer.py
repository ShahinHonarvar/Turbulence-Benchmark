
import re

def all_left_right_truncatable_prime(n):
    #range = [x for x in range(2,n+1) if x%2==1 and all(x%10!=0 for x in range(x,x+10,1))]
    # return range
    # return [x for x in range(2,n+1) if x%2==1 and all(x%10!=0 for x in range(x,x+10,1)) and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==1]
    # return [x for x in range(2,n+1) if x%2==1 and x%10!=0]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0 and x%10!=0]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0 and x%10!=0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0 and x%10!=0 and x%10!=0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and x%10==0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x%10!=0 and x not in range(n//2+1,n+1,2)]
    # return [x for x in range(2,n+1) if x%2==1 and
