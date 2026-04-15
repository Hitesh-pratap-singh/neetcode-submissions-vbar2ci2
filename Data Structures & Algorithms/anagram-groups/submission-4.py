class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_array = {}

        for s in strs:
            temp = "".join(sorted(s))
            
            freq_array[temp] = freq_array.get(temp, []) + [s]

        return list(freq_array.values())


