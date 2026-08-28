class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        odd_chars = []
        for ch, freq in counts.items():
            if freq % 2 != 0:
                odd_chars.append(ch)
                
        if len(odd_chars) > 1:
            return ""
            
        mid_char = odd_chars[0] if odd_chars else ""
        
        half_counts = {}
        for ch, freq in counts.items():
            if freq // 2 > 0:
                half_counts[ch] = freq // 2
                
        N = len(s)
        half_N = N // 2
        

        max_i = 0
        curr_counts = dict(half_counts)
        for i in range(half_N):
            ch = target[i] if i < len(target) else ""
            if ch in curr_counts and curr_counts[ch] > 0:
                curr_counts[ch] -= 1
                max_i += 1
            else:
                break

        if max_i == half_N:
            L = target[:half_N]
            P = L + mid_char + L[::-1]
            if P > target:
                return P
                

        start_i = min(max_i, half_N - 1)
        
        rem_counts = dict(half_counts)
        for i in range(start_i):
            rem_counts[target[i]] -= 1
            
        for i in range(start_i, -1, -1):
            target_char = target[i] if i < len(target) else ""
            

            valid_chars = []
            for ch, v in rem_counts.items():
                if v > 0 and ch > target_char:
                    valid_chars.append(ch)
                    
            if valid_chars:

                best_char = min(valid_chars)
                rem_counts[best_char] -= 1
                

                rest_chars = []
                for ch, v in rem_counts.items():
                    if v > 0:
                        rest_chars.extend([ch] * v)
                rest_chars.sort()
                
                prefix = target[:i]
                L = prefix + best_char + "".join(rest_chars)
                return L + mid_char + L[::-1]
 
            if i > 0:
                rem_counts[target[i-1]] += 1
                
        return ""