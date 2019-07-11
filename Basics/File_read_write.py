# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:31:45 2019

@author: Yusef Quinlan
"""
#Open a file and use the file name and the letter representing what we want to do with the file
# For read it would be open('file.filetype', 'r') r represents 'read' to read a file
# For write it would be open('file.filetype', 'w') w represents 'write' to write a file
# For append it would be open('file.filetype', 'a') a represents 'append' to append to a file
f = open('test.txt', 'r')
print(f.name)
#close the file with .close()
f.close()
#print the mode using variable.mode where variable references a file object,
# this will get the mode i.e. 'w' for write, 'r' for read, 'a' for append.
print(f.mode)
#Instead of directly closing the file with explicit use of close(),
# it is possible to write into a context manager using :
#   with open(file.filetype, mode) as:
#in this block you can modify your code and once the block ends the file will 
# close automatically
with open('test.txt', 'r') as f:
    print(f.name)
    print(f.mode)

#We can now use read() to read the file contents, by sticking the read value
# into a variable we should be able to use the variable outside of the context manager
# i.e. outside of the with open BLOCK
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
    
f_contents_altered = f_contents + 'lolthis file has been ALTERED'
print(f_contents_altered)

#One line can be read if needed i.e.:
with open('test.txt', 'r') as fi:
    f_contents2 = fi.readline()
    print(f_contents2)
    
#readline reads one unread line so two executions of readline() would read the first 2 lines:
with open('test.txt', 'r') as f2:
    f_contents3 = f2.readline()
    print(f_contents3)
    f_contents3 = f2.readline()
    print(f_contents3)
    
#Same as above but get rid of the /n newlines so there is no space between lines
with open('test.txt', 'r') as f2:
    f_contents3 = f2.readline()
    print(f_contents3, end='')
    f_contents3 = f2.readline()
    print(f_contents3, end = '')

# to iterate over the entire text file and have no spaces between lines use a for loop of for line in variable
with open('test.txt', 'r') as f3:
    for line in f3:
        print(line, end='')

#now it is time to write to an existing file with the write mode 'w', note that
# if the file does not exist it will be written into existence i.e. a new file will be made
# note that if you use the write() method it will overwrite the entire file
# if you use the write method twice in the WITH OPEN block, then both write functions will be written
# into the file, the file will be overwritten but the write function will not overwrite eachother.
with open('test2.txt', 'w') as f4:
    f4.write('hellz yeah ')
    f4.write('I am such a boss dude!')
    





    

      