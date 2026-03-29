#1
#УИС-211
stroka = "Python Programming"
words = stroka.split()
for word in words:
    print(word)

3
a = str(input())
result = ""
for i in range(len(a)):
    if a[i] not in result:
        result+=a[i]
print(result)

2
string = str(input())
count = False
if string == string[::-1]:
    count = True
else:
    count = False
print(count)
4
a = str(input())
longest = ""
for i in range(len(a)):
    cur_str = ""
    for j in range(i,len(a)):
        char = a[j]
        if char in cur_str:
            break
        cur_str+=char
    if len(cur_str) > len(longest):
        longest = cur_str
print(longest)
#5
string = str(input())
if not string:
    print(string)
else:
    compress = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count +=1
        else:
            compress += string[i-1] + str(count)
            count = 1

    compress +=string[-1] + str(count)
    if len(compress) < len(string):
        print(compress)
    else:
        print(string)
