
import sys
input = sys.stdin.readline

def all_left_right_truncatable_prime(n):
    # from functools import lru_cache
    # @lru_cache(maxsize=1_000_000)
    # def is_left_right_truncatable_prime(n):
    #     # return all(int(d) for d in str(n) if d!='0' and int(d) not in (1,2))
    #     return all(int(d) not in (1,2) for d in str(n))
    #     return True
    # return is_left_right_truncatable_prime(n)
    # return [n for n in range(2, n+1) if is_left_right_truncatable_prime(n)]
    # return [n for n in range(2, n+1) if all(int(d) not in (1,2) for d in str(n))]
    # return [n for n in range(2, n+1) if all(int(d) not in (1,2) for d in str(n) if d!='0')]
    # return [n for n in range(2, n+1) if all(int(d) not in (1,2) for d in str(n) if d!='0') and n>1]
    # return [n for n in range(2, n+1) if all(int(d) not in (1,2) for d in str(n) if d!='0') and n>1 and n%2==0]
    # return [n for n in range(2, n+1) if all(int(d) not in (1,2) for d in str(n) if d!='0') and n>1 and n%2==0 and int(str(n)[-1]) not in (1,2)]
    # return [n for n in range(2, n+1) if all(int(d) not in (1,2) for d in str(n) if d!='0') and n>1 and n%2==0 and int(str(n)[-1]) not in (1,2) and int(str(n)[0]) not in (1,2)]
    # return [n for n in range(2, n+1) if all(int(d) not in (1,2) for d in str(n) if d!='0') and n>1 and n%2==0 and int(str(n)[-1]) not in (1,2) and int(str(n)[0]) not in (1,2) and int(str(n)[1]) not in (1,2)]
    # return [n for n in range(2, n+1) if all(int(d) not in (1,2) for d in str(n) if d!='0') and n>1 and n%2==0 and int(str(n)[-1]) not in (1,2) and int(str(n)[0]) not in (1,2) and int(str(n)[1]) not in (1,2) and int(str(n)[2]) not in (1,2)]
    # return [n for n in range(2, n+1) if all(int(d) not in (1,2) for d in str(n) if d!='0') and n>1 and n%2==0 and int(str(n)[-1]) not in (1,2) and int(str(n)[0]) not in (1,2) and int(str(n)[1]) not in (1,2) and int(str(n)[2]) not in (1,2) and int(str(n)[3]) not in (1,2)]
    # return [n for n in range(2, n+1) if all(int(d) not in (1,2) for d in str(n) if d!='0') and n>1 and n%2==0 and int(str(n)[-1]) not in (1,2) and int(str(n)[0]) not in (1,2) and int(str(n)[1]) not in (1,2) and int(str(n)[2]) not in (1,2) and int(str(n)[3]) not in (1,2) and int(str(n)[4]) not in (1,2)]
    # return [n for n in range(2, n+1) if all(int(d) not in (1,2) for d in str(n) if d!='0') and n>1 and n%2==0 and int(str(n)[-1]) not in (1,2) and int(str(n)[0]) not in (1,2) and int(str(n)[1]) not in (1,2) and int(str(n)[2]) not in (1,2) and int(str(n)[3]) not in (1,2) and int(str(n)[4]) not in (1,2) and int(str(n)[5]) not in (1,2)]
    # return [n for n
