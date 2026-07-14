class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       n=len(nums)
       for i in range(1,n):
             start = 0

             while start < i:
                 if nums[start] + nums[i] == target:
                     return [start,i]
                 start += 1
       return []                  