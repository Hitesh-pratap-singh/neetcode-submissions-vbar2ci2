class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        if len(strs) == 1:
            return [strs]

        freq_array = {}

        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))

            if temp in freq_array:
                freq_array[temp].append(strs[i])
            else:
                freq_array[temp] = [strs[i]]

            print(freq_array)

        for key, value in freq_array.items():
            result.append(value)

        return result


