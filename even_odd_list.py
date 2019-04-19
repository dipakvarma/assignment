list=[2,12,17,18,19,6,5,3]
even=[]
odd=[]
s=','
for num in list:
        if num%2==0:
                even.append(num)
        else:
                odd.append(num)
print'even',even,
print'\nodd',odd,
