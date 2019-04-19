string='google.com'
a={}

for i in string:
        if i in a:
                a[i]+=1
        else:
                a[i]=1
print 'characters are:'+str(a)
