input1 = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(input1+"\n")
    print("Data successfully written to output.txt")
input2 = input("Enter additional text to append: ")
with open("output.txt", 'a') as file:
    file.write(input2+"\n")
    print("Data successfully appended")


print(f'Final content of output.txt: ')
with open("output.txt",'r') as file:
    for line in file:
        print(line.strip())
