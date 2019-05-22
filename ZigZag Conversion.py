class Solution:
    def convert(self, s, numRows):
        if numRows == 1: return s
        words, n = [""] * numRows, numRows - 1
        for i, c in enumerate(s):
            idx = n - i % n if (i // n) & 1 else i % n
            words[idx] += c
        return "".join(words)
        
#I like the upper one 

class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        res, gap = "", 2*(numRows-1)
        for i in range(numRows):
            tmp = i
            while tmp < len(s):
                res += s[tmp]
                # special cases 
                if i != 0 and i != numRows-1: 
                    if tmp+gap-2*i < len(s):
                        res += s[tmp+gap-2*i]
                tmp += gap
        return res

    
            
