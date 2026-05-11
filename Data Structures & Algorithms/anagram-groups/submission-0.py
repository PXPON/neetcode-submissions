class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = []

        anagram_dict = dict()

        for s in strs:
            s_array = list(s)
            s_array.sort()
            s_arranged = "".join(s_array)

            # Check to see if the array is in anagram_dict
            if s_arranged in anagram_dict:
                # Append s to the list value for the key
                anagram_dict[s_arranged].append(s)
            else:
                anagram_dict[s_arranged] = [s]

        for k in anagram_dict:
            group_anagrams.append(anagram_dict[k])
        
        return group_anagrams