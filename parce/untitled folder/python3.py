ints_list=[]
for line in open('title.txt').readlines():
    url = line.split()
    ints_list.append(url)
for x in ints_list:
    if ints_list.count(x) > 1: 
        ints_list.remove(x) 
with open("titlesur.txt", "a") as file:
    print(*ints_list, file=file, sep="\n") 
