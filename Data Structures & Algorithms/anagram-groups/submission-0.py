class Solution:
    def helper(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        if len(strs) == 1:
            return [strs]

        seen_index = set()

        for i in range(len(strs)):
            if i in seen_index:
                continue
            temp = [strs[i]]
            for j in range(i+1, len(strs)):
                if j in seen_index:
                    continue
                check = self.helper(strs[i], strs[j])
                if check:
                    temp.append(strs[j])
                    seen_index.add(j)
                j += 1
            i+=1
            print(temp)
            result.append(temp)

        return result
