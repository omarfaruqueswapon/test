T = int(input())
names=[]
for tc in range(T):
	# Read integers a and b.
	names.append(list(input().split(" ")))

for i in range(len(names)):
	if  len(names[i])==1:
		continue
	if  len(names[i])==2:
		names[i][0]=names[i][0][0].capitalize()+"."
		print(names[i])
	if  len(names[i])==3:
		names[i][0]=names[i][0][0].capitalize()+"."
		names[i][1]=names[i][1][0].capitalize()+"."
		print(names[i])
		
print(names)