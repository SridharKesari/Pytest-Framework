try:
    # f = open('myfile.txt', 'r')
    # print(f.read())
    f = open('myfile.txt', 'r')
    # print(f.readline(), end='') # only the
    # print(f.readline())  # only the
    # f = open('myfile.txt', 'r')
    # print(f.readlines())    # as a list
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
finally:
    f.close()

print("****using with option*****")
with open('myfile.txt', 'r') as f:
    # print(f.readline())
    # list2 = f.read().split('\n')
    # print(list2)

    for line in f:
        print(line.strip())
