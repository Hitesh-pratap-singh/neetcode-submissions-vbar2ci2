class Solution:
    # def helper(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False

    #     count = [0] * 26
    #     for i in range(len(s)):
    #         count[ord(s[i]) - ord('a')] += 1
    #         count[ord(t[i]) - ord('a')] -= 1

    #     for val in count:
    #         if val != 0:
    #             return False
    #     return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        if len(strs) == 1:
            return [strs]

        # seen_index = set()

        # for i in range(len(strs)):
        #     if i in seen_index:
        #         continue
        #     temp = [strs[i]]
        #     for j in range(i+1, len(strs)):
        #         if j in seen_index:
        #             continue
        #         check = self.helper(strs[i], strs[j])
        #         if check:
        #             temp.append(strs[j])
        #             seen_index.add(j)
        #     print(temp)
        #     result.append(temp)

        ascii_sum_array = {}

        for i in range(len(strs)):
            temp_sum = 0
            for j in range(len(strs[i])):
                temp_sum += ord(strs[i][j])
            print(temp_sum)
            if temp_sum in ascii_sum_array:
                ascii_sum_array[temp_sum].append(strs[i])
            else:
                ascii_sum_array[temp_sum] = [strs[i]]
            # print(ascii_sum_array)
        print(ascii_sum_array)

        for key, value in ascii_sum_array.items():
            result.append(value)
        return result

        # return result
