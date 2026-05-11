class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Boolean AND on each of the numbers
        # -10,000 to 10,000 means 15-bit resolution
        
        # Initial value needs to be all 1's
        bin_output = 0

        for num in nums:
            bin_output = bin_output ^ num

        return bin_output