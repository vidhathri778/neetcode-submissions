class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        max_c=0
        for i in nums:
            if i==1:
                c+=1
                max_c=max(c,max_c)
            else:
                c=0
        return max_c