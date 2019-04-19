def remove(string, n):  
      first = string[:n]   
      last = string[n+1:]  
      return first + last
print(remove('hello',0))
