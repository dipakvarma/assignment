def remove_odd(string):
        new_string= ""

        for i in range(len(string)):
                if i%2 == 0:
                        new_string=new_string + string[i]
        return new_string
        
print remove_odd("deepak")
                 
