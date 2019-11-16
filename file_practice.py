my_list = ["a", "b", "c"]

my_file = open("demoTextFile.txt", "w")

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()
