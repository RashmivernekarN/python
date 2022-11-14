# Program to show various ways to read and
# write data in a file.
file1 = open("Myfile1.txt","a")

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
L = ["This is Dharwad \n","This is Hubli \n","This is Belgaum \n"]
file1.writelines(L)
file1.close() #to change file access modes

file1 = open("Myfile1.txt","r+")
print("Output of Read function is ")
print(file1.read())
# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)
print( "Output of Readline function is ")
print(file1.readline())

file1.seek(0)
# To show difference between read and readline
print("Output of Read(100) function is ")
print(file1.read(100))
file1.seek(0)
print("Output of Readline(9) function is ")
print(file1.readline())
file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines()[3])
file1.close()
