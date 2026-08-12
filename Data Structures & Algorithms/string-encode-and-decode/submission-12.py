class Solution:

    def encode(self, strs: List[str]) -> str:
        mes = ""
        if len(strs) == 0:
                return "XXXXXXXXXXXXXX"

        for i in range(len(strs)):
            # Replace spaces in strs[i] with characters
            strs[i] = strs[i].replace(" ", "****")
            mes += strs[i]

            if i < len(strs) - 1 and len(strs) != 0:
                mes += " "
        
        return mes


    def decode(self, s: str) -> List[str]:
        if s == "XXXXXXXXXXXXXX":
            return []

        # Delimit by spaces
        new_array = s.split(" ")

        # Go through each item and replace
        for i in range(len(new_array)): 
            new_array[i] = new_array[i].replace("****", " ")

        return new_array
