#Fascinating Number :- When 3 digit number (n) is concatenated with the number multipiled by 2 i.e. (n*2) and with 3 i.e. (n*3) and we get number which contains all the digit from 1 to 9 exactly once.
#EX:- i/p - Enter the 3 digit number= 273
#	o/p- 273 is fascinating number.
#Expalnaton- 273*1 = 273, 273*2 = 546 , 273*3 = 819 after concatenating this result we get 273546819, in this we get 1 to 9 number exactly once.




def isFascinating(n):
	strNum = str(n) + str(n*2) + str(n*3)
	freq = [0]*11

	for i in range(len(strNum)):
		digit =int(strNum[i])
		freq[digit] += 1

	for i in range(1,10):
		if freq[i] == 0:

			return False
	return True

num = int(input("Enter the 3 digit number : "))

if(isFascinating(num)) :
	print(num," is fascinating")		
else:
	print(num,"is not fascinating")

