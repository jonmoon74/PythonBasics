my_file = open("demoTextFile.txt", "r")
my_list = []

for line in my_file.readlines():
    my_list.append(str(line))

my_file.close()
print(my_list)
