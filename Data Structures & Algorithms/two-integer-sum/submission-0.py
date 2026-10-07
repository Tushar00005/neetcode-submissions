class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_container={}
        for index,num in enumerate(nums):
            complement=target-num
            if complement in num_container:
                return [num_container[complement], index]
            num_container[num]=index
        
        
            
        