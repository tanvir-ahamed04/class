# 4. File Handling
with open("sample.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")
with open("sample.txt", "r") as file:
    content = file.read()
    print("Contents of sample.txt:")
    print(content)
