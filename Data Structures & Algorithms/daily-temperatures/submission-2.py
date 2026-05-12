class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        forecast = [0] * len(temperatures)

        # Put each value on stack one at a time and compare
        # for i in range(1, len(temperatures) + 1):
        for i in range(len(temperatures)):
            # Check to see if temp is >= what's at the top of the stack

            if stack == []:
                stack.append(i)

            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Don't append
                # Add currentIndex - previousIndex to previousIndex
                val = stack.pop()
                forecast[val] = i - val
            stack.append(i)
        
        return forecast
            