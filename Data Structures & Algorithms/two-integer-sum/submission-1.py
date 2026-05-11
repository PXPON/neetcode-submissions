class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        
        i = 0
        while i < len(nums):
            # Twos compliment
            diff = target - nums[i]

            # Check to see if target - num is in hash
            if diff in hash:
                # Return its value which is the index it sits on
                return [hash[diff], i]
            else:
                hash[nums[i]] = i
            i += 1

        return []
        