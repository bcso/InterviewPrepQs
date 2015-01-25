class Solution:
    # @return an integer
    def atoi(self, str):
        sign = 1
        cleanStrRep = ""
        for x in xrange(str):
            if char == " ": 
                continue
            
            if char == "-":
                sign = -1
            
            if char == "+":
                sign = 1
            
            if char not in ["1","2","3","4","5","6","7","8","9","0"]:
                continue
            
            cleanStrRep.append(str[x])
        
        return sign*int(cleanStrRep)