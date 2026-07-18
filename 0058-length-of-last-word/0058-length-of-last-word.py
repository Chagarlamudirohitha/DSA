class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s[::-1]
        i=0
        print(s)
        a=[]
        if len(s)==1 and s!=" ":
            return 1
        if len(s)==1 and s==" ":
            return 0    
        while(s[i]==' '):
            i+=1
           
        while(s[i]!=' '):
            a.append(s[i])
            if i==len(s)-1:
                break
            i+=1
        print(a)    
        return len(a)    


