import re
# import urllib.request,urllib.parse,urllib.error
fhand = open('comments_552553.html')
# counts = dict()

sum = 0

for line in fhand:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number)

print(sum)