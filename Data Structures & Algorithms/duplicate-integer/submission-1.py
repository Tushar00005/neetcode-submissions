class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=len(nums)!=len(set(nums))
        return a