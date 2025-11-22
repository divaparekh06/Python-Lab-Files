# f1 = open(r"C:\Users\Diva Parekh\Downloads\ict.txt")
# for each in f1:
#     print (each)
# print (f1.read())

# f1 = open(r"C:\Users\Diva Parekh\Downloads\ict.txt")
# print (f1.read(5))

# with open(r"C:\Users\Diva Parekh\Downloads\ict.txt",'r') as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print (word)

# file = open("ict1.txt",'a')
# file.write("\n Department Department")
# file.close()

# with open(r"C:\Users\Diva Parekh\Downloads\a (1).tif", 'rb') as file:
#      binary_data = file.read()

# with open('c.tif', 'wb') as f:
#     f.write(binary_data)
#     f.close()

# import csv
# # Reading from a CSV file
# with open('data-1.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# import csv
# with open('output.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Subject', 'Mark'])
#     writer.writerow(['Ansh', 'PWP', 9])
#     writer.writerow(['Ashutosh', 'PWP', 10])
#     file.close()

#---------POST LABS----------

#Question 1
# with open("ict1.txt", 'r') as f: 
#     text = f.read() 
 
# lines = text.splitlines() 
# words = text.split() 
# chars = len(text) 
 
# print("Lines:", len(lines)) 
# print("Words:", len(words)) 
# print("Characters:", chars) 

#Question 2
# list = [] 
# with open("ict1.txt", 'r') as f: 
#     for line in f: 
#         list.append(line.strip()) 
 
# print(list)

#Question 3
# import csv 
 
# with open('output.csv', 'r') as file: 
#     reader = csv.reader(file)
# for row in reader: 
#         print(row)

#Question 4
# with open("ict.txt", 'r') as f1, open("ict1.txt", 'r') as f2, open("merged.txt", 'w') as fout: 
#     fout.write(f1.read()) 
#     fout.write("\n") 
#     fout.write(f2.read())








