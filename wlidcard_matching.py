class Solution:
    def is_match(self, s, p, s_idx, p_idx):
	    # reached end of both strings, it must have matched
        if s_idx >= len(s) and p_idx >= len(p):
            return True
  
		# reached end of s, but there are still characters in p remaining
        if s_idx >= len(s) and p_idx < len(p):
		    # if any character remaining in p, is not "*"
			# that means we have nothing in s to match, so return False
            for i in range(p_idx, len(p)):
                if p[i] != "*":
                    return False
            return True
        
		# if we have reached end of p, but not end of s, this means
		# we do not have sufficient characters in the pattern to match s
		# return false
        if s_idx < len(s) and p_idx >= len(p):
            return False
        
        if (s_idx, p_idx) in self.dp:
            return self.dp[(s_idx, p_idx)]
        
        s_char = s[s_idx]
        p_char = p[p_idx]
        
        if p_char.isalpha() and s_char != p_char:
            return False
        
        if p_char == "*":
            skip_star = self.is_match(s, p, s_idx, p_idx + 1)
            use_star = self.is_match(s, p, s_idx + 1, p_idx)
            not_use_star = self.is_match(s, p, s_idx + 1, p_idx + 1)
            
            self.dp[(s_idx, p_idx)] = skip_star or use_star or not_use_star
            return self.dp[(s_idx, p_idx)]
        
        self.dp[(s_idx, p_idx)] = self.is_match(s, p, s_idx + 1, p_idx + 1)
        return self.dp[(s_idx, p_idx)]        


    def isMatch(self, s: str, p: str) -> bool:        
        self.dp = {}
        return self.is_match(s, p, 0, 0)
