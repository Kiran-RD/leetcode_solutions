class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_idx = [i for i in range(len(s)) if s[i] == c]
        res = []
        i,l,r,j = 0,'-inf',c_idx[0],0
        while i < len(s):
            if l == '-inf':
                res.append(r-i)
            elif r == 'inf':
                res.append(i-l)
            elif i<(l+r)/2 :
                res.append(i-l)
            else: res.append(r-i)

            i += 1
            if j < len(c_idx) and i > c_idx[j] :
                l = c_idx[j]
                j += 1
                if j < len(c_idx):
                    r = c_idx[j]
                else:
                    r = 'inf'

        return res
