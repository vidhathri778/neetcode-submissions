class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1={}
        dict2={}
        for ch1 in s:
            if ch1 in dict1:
                dict1[ch1]+=1
            else:
                dict1[ch1]=1
        for ch2 in t:
            if ch2 in dict2:
                dict2[ch2]+=1
            else:
                dict2[ch2]=1
        return dict1==dict2