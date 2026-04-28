class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1
        
        required = len(t_freq)
        matches = 0
        window = {}
        l = 0
        min_len = float('inf')
        result = ""
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            # when does matches increment?
            if c in t_freq and window[c]==t_freq[c]:
                matches += 1
            
            # when do we shrink?
            while matches == required:
                # record minimum window
                if min_len > (r-l+1):
                    min_len = r - l + 1
                    result = s[l:r+1]
                
                # shrink from left
                left_c = s[l]
                window[left_c] -= 1
                if left_c in t_freq and window[left_c]<t_freq[left_c]:
                    matches -= 1
                l += 1
        
        return result