string = input("Enter the string : ")
j = 0
str1 = ""
temp = 0
str = list(string)

for i in range(0, len(str)):
	for j in range(0, len(str)):
		if(str[j] > str[i]):
			temp = str[i]
			str[i] = str[j]
			str[j] = temp
print("The sorted string is : ")
print(str1.join(str))
