class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        if len(s)!=len(t):
            return False
        ch1={}
        ch2={}
        for i in s:
            if i in ch1:
                ch1[i]+=1
            else:
                ch1[i]=1
        for j in t:
            if j in ch2:
                 ch2[j]+=1
            else:
                 ch2[j]=1
        return ch1==ch2       

        
       