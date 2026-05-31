class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        c=0
        for i in nums:
            if i!=1:
                c=0
            else:
                c+=1
            ans = max(ans, c)
        return ans