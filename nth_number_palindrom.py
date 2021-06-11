# This code is to find nth Palindrom number. 

class Palindrom:
    #  Magic method
    def __init__(self, number):
        self.number = number
    
    # checking the value is palindrom or not 
    def __is_palindrom(self, value):
        k = value
        if str(k) == str(value)[::-1]:
            return True
    
    # get method 
    def get_value(self):
        iter = 1            # initializing numbers to iteret 
        index = 0           # initializing index
        while index != self.number:     # loop to check the index
            if self.__is_palindrom(iter):       # checking for palindrom
                index = index + 1
                iter = iter + 1
            else:
                iter = iter + 1
        return iter-1           # returning the required value

if __name__ == "__main__":
    # user input
    user = int(input("Index you required: "))
    obj = Palindrom(user)
    print(obj.get_value())
