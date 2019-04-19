str='Tech_Receptive123@gmail.com'

capital,lower,number,special=0,0,0,0

for i in str:
        if (i.isupper()):
                capital +=1
        elif(i.islower()):
                lower +=1
        elif(i.isdigit()):
                number +=1
        else:
                special +=1
print 'capital characters:',capital
print 'lower characters:',lower
print 'numbers:',number
print 'special characters:',special
