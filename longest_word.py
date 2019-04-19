words=['apple','banana','pineapple']
for i in range(len(words)-1):
	if len(words[i]) > len(words[i+1]):
		largest = words[i]	
	else:
		largest = words[i+1]
print largest

