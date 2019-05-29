#HARDCODING EVERY CASE BASED ON STRINGS
class Solution:
    def myAtoi(self, str: str) -> int:
        x=1
        y=1
        p=1
        ans=""
        for i in str:
            if p==0 and i==' ' or i=="  ":
                break
            elif i==' ' or i=='   ':
                pass
            elif i=='-' and y and p:
                x=-1
                y=0
                p=0
            elif i=='+' and y and p:
                y=0
                x=1
                p=0
            elif ord(i)<58 and ord(i)>47:
                ans+=i
                p=0
            
            else:
                break
        if len(ans)==0:
            ans='0'
        if x*int(ans)<-2**31:
            return -2**31
        elif x*int(ans)>(2**31-1):
            return 2**31-1
        else:
            return x*int(ans)
            
#BETTER SOLUTION I FOUND WITH REGEX
class Solution:
    def myAtoi(self, str):
        numberStr = re.findall('^[\+\-]?0*\d+', str.strip())
        
        if numberStr:
            number = int(numberStr[0])
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if number < MIN_INT:
                return MIN_INT
            elif number > MAX_INT:
                return MAX_INT
            else:
                return number
        else:
            return 0
            
