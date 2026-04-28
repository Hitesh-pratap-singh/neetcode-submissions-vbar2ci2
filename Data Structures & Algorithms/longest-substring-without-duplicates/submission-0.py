class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        if len(s) == 0:
            return max_len

        l,r = 0, 1

        seen = set()
        seen.add(s[l])
        while r<len(s) and l<len(s):
            print(seen)
            if s[r] not in seen:
                seen.add(s[r])
                max_len = max(r-l+1, max_len)
                r+=1  
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[l])
                l += 1
                seen.add(s[r])
                max_len = max(r-l+1, max_len)
                r += 1

        return max_len