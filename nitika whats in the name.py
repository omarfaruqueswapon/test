T = int(input())
names=[]
for tc in range(T):
	# Read integers a and b.
	names.append(list(input().split(" ")))

for i in range(len(names)):
	if  len(names[i][0])>1 and len(names[i])==1:
		print(names[i][0])
	if len(names[i][0])>1:
		print(names[i][0][0].capitalize()+".")
	if len(names[i][1])>1:
		print(names[i][1][0].capitalize()+".")
		
		