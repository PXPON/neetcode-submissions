class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if nums[mid] == target:
                return mid


            # Set left or right to mid
            # Subtract from right and add to left
            # Because we want to skip places we know aren't good

            if target < nums[mid]:
                right = mid - 1
            else:
                # Set right one over
                left = mid + 1

        return -1