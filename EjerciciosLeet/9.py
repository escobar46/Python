class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Convierto x en una cadena 
        x_cade= str(x)
        #Ya convertido en una cadena lo invierto
        x_revers= x_cade[::-1]
        #Con los dos los comparo con un if y que me retorne lo que necesito
        if x_cade==x_revers:
            return True 
        else: 
           return False
        