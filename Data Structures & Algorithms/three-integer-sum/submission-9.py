class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        triplets = []
        nums.sort()

        i = 0; j = 1; k = 2
        # Check to see if all three add up
        # nums appears to be sorted

        for i in range(len(nums) - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i -1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0 and [nums[left], nums[right], nums[i]] not in triplets:
                    triplets.append([nums[left],nums[right],nums[i]])
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
            
        return triplets