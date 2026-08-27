from itertools import permutations

class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        n = len(s)
        res = []
        
        
        for i in range(n):
            t_char = target[i] if i < len(target) else ''
            

            available_chars = sorted([k for k, v in counts.items() if v > 0])
            placed = False
            
            for c in available_chars:
                if c > t_char:

                    res.append(c)
                    counts[c] -= 1
                    

                    for rem_c in sorted(counts.keys()):
                        if counts[rem_c] > 0:
                            res.append(rem_c * counts[rem_c])
                    return "".join(res)
                
                elif c == t_char:

                    counts[c] -= 1
                    
                    max_remaining_list = []
                    for k in sorted(counts.keys(), reverse=True):
                        if counts[k] > 0:
                            max_remaining_list.append(k * counts[k])
                    max_remaining = "".join(max_remaining_list)
                    
                    target_remaining = target[i+1:]
                    
                    if max_remaining > target_remaining:
                        res.append(c)
                        placed = True
                        break
                    else:

                        counts[c] += 1
            
            if not placed:
                return ""
                
        return "".join(res)