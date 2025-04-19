class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)

        for i in nums:
            dict[i]=dict.get(i,0)+1

        s=list(dict.keys())

        for i in s:
            if(dict[i]>(n/2)):
                return i
