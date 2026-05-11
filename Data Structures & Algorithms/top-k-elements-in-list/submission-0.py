import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a hashmap
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        
        # With the hash map populated
        # Create a heap
        # This is to reduce down to our Top K
        heap = []

        # Order the heap by frequency
        for num, freq in count.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)

        returnArray = []
        for freq, num in heap:
            returnArray.append(num)

        return returnArray

        