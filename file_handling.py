try:
    count = 1
    with open("sample.txt", "r") as file:
        print(f'Reading file content: ')
        for line in file:
            print(f'Line {count} : {line.strip()}')
            count+=1  
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

