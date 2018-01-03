import os
from collections import Counter
from shutil import copyfile
import random

print "Current Working Directory:", os.getcwd()

# Basic File I/O Tutorial and quick reference to popular problems

# Problems
# 1) Read and print an entire text file.
# 2) Read a file one character at a time.
# 3) Read first n lines of a file.
# 4) Append text to a file and display the text.
# 5) Read a file line by line and store it into a list.
# 6) Read a file line by line and store it into a variable.
# 7) Find the longest string(s) in a file.
# 8) Count the number of lines in a text file.
# 9) Count the frequency of words in a file.  Also display the top 3.
# 10) Count the frequency of letters/numbers/symbols in a file.
# 11) Count the frequency of equivalent lines in a file.
# 12) Get the file size of a plain file.
# 13) Write a list to a file.
# 14) Write a program based on user input that either overwrites, appends to, or does nothing to a file.
#     If the given file name doesn't exist, create it as a new file and write data to it.
# 15) Copy the contents of a file to another file.
# 16) Append a files contents to another file.
# 17) Reverse contents of a file and write the result to a new file.
# 18) Determine if a file is closed or not.
# 19) Read a random line from a file.

# -------------------------------------------------------------------

# Question 1
# Read and print an entire text file.

def read_whole_file(filename):
    try:
        with open(filename, "r") as foo:
            print "Contents of file {}:".format(filename)
            for line in foo:
                print line,
    except IOError:
        print "{} does not exist! Enter a file that exists".format(filename)
  
filename = raw_input("Enter file name:")
read_whole_file(filename)

# -------------------------------------------------------------------

# Question 2
# Read a file one character at a time.

def read_one_char(filename):
    try:
        with open(filename, "r") as foo:
            line = foo.read(1)
            while line != "":
                print line,
                line = foo.read(1)
    except IOError:
        print "{} does not exist! Enter a file that exists".format(filename)
  
filename = raw_input("Enter file name:")
read_one_char(filename)

# -------------------------------------------------------------------

# Question 3
# Read first n lines of a file.

def read_n_lines(filename, n):
    try:
        with open(filename, "r") as foo:
            for i in xrange(n):
                line = foo.readline()
                print line,
    except IOError:
        print "{} does not exist! Enter a file that exists".format(filename)
  
filename = raw_input("Enter file name:")
lineNumber = int(raw_input("How many lines of the file would you like to read?"))
read_n_lines(filename, lineNumber)

# -------------------------------------------------------------------

# Question 4
# Append text to a file and display the text.
# See Q14 to write multiple lines to a file

def append_content(filename, added_text):
    with open(filename, "a+") as foo:
        foo.write(added_text)
        foo.seek(0) # Back to start of file
        print "File {} after write:".format(filename)
        for line in foo:
            print line,

filename = raw_input("What is your filename?")
added_text = raw_input("Enter the text you want to add to {}".format(filename))
append_content(filename, '\n' + added_text)

# -------------------------------------------------------------------

# Question 5
# Read a file line by line and store it into a list.

def list_format(filename):
    try:
        with open(filename, "r") as foo:
            content = foo.readlines() # readline() creates a list of the file contents.
            print content
    except IOError:
        print "{} does not exist! Enter a file that exists".format(filename)

filename = raw_input("Enter file name: ")
list_format(filename)

# -------------------------------------------------------------------

# Question 6
# Read a file line by line and store it into a variable.

def store_line_as_variable(filename):
    try:
        with open(filename, "r") as foo:
            currentLine = ""
            for line in foo:
                # print line
                currentLine = currentLine + line
                # print currentLine # See how the variable grows larger with the files contents after each iteration
            return currentLine
    except IOError:
        print "{} does not exist! Enter a file that exists".format(filename)

filename = raw_input("What is your filename?")
print store_line_as_variable(filename)

# -------------------------------------------------------------------

# Question 7
# Find the longest string(s) in a file.

# To preface this question we will show examples of how to break the files contents into pieces
with open("test.txt", "r") as foo:
    # f_contents1 is a STRING of the whole files contents
    # Example: 'Hello my name is Drew\nNice to meet you!\nWhere are you from?\n.......'
    f_contents1 = foo.read() # Use debug window to see how contents are stored in variable
    print f_contents1
    foo.seek(0)
    print '\n'

    # f_contents2 is a STRING of the first line of the file
    # Example: 'Hello my name is Drew\n'
    f_contents2 = foo.readline() # Use debug window to see how contents are stored in variable
    print f_contents2
    foo.seek(0)
    print '\n'

    # f_contents3 is a LIST of STRINGS. Each element in the list is a line in the file
    # Example: ['Hello my name is Drew\n', 'Nice to meet you\n', Where are you from?\n', .........]
    f_contents3 = foo.readlines() # Use debug window to see how contents are stored in variable
    print f_contents3
    foo.seek(0)
    print '\n'

    # f_contents4 is a LIST of STRINGS.  Difference is that each element is a a word in the file thanks to the split() method
    # Example: ['Hello', 'my', 'name', 'is', 'Drew']
    f_contents4 = foo.read().split() # Use debug window to see how contents are stored in variable
    print f_contents4
    foo.seek(0)
    print '\n'

    # When you're working with large files, it is usually best to iterate over the file instead of saving all the files contents in a variable
    # Choose which is best for your program

    # Prints out all the files contents one character at a time
    for line in foo.read():
        print line
    foo.seek(0)
    print '\n'

    # Prints out the files first line one character at a time
    for line in foo.readline():
        print line
    foo.seek(0)
    print '\n'

    # Prints out the files contents one line at a time
    for line in foo.readlines():
        print line,
    foo.seek(0)
    print '\n'

    # Prints out the files contents one line at a time. Similar to for line in foo.readlines()
    for line in foo:
        print line,
    foo.seek(0)
    print '\n'

    # Print out the files contents one word at a time all on one line.  No newline.
    for line in foo.read().split():
        print line,
    foo.seek(0)
    print '\n'

# Answer to Question 7
# Use split() method and keep track of each strings character length.
def longest_word(filename):
    try:
        with open(filename, 'r') as foo:
            words = foo.read().split()
        max_len = len(max(words, key=len))
        return [word for word in words if len(word) == max_len] # Iteration is needed in case there are more than one word with the same length.

        # List comprehensions are one of Python's best features
        # Clear and concise code is attractive.
        # [word for word in words if len(word) == max_len] is equivalent to:
        #for word in words:
            #if len(word) == max_len:
                #return word''
    except IOError:
        print "{} does not exist! Enter a file that exists".format(filename)

filename = raw_input("What is your filename?")
longestWord = longest_word(filename)
print "Longest word(s) in file {} are: {}".format(filename, longestWord)


# -------------------------------------------------------------------

# Question 8
# Count the number of lines in a text file.

def line_count(filename):
    try:
        with open(filename, "r") as foo:
            for lineCount, line in enumerate(foo):
                pass
            return lineCount + 1
            # Index starts at 0, so our first line is counted as 0 istead of 1.  Thus, add 1 to the final lineCount variable
    except IOError:
        print "{} does not exist! Enter a file that exists".format(filename)

filename = raw_input("What is your filename?")
lineCount = line_count(filename)
print "There are {} lines in the file {}".format(lineCount, filename)


# -------------------------------------------------------------------

# Question 9
# Count the frequency of words in a file.  Also display the top 3.

def word_frequency(filename):
    try:
        with open(filename, "r") as foo:
            words = foo.read().lower().split()
            return Counter(words), Counter(words).most_common(3)
    except IOError:
        print "{} does not exist! Enter a file that exists".format(filename)

filename = raw_input("What is your filename?")
wordFreq, topThree =  word_frequency(filename)
print "Word Frequencies: {}\n".format(wordFreq)
print "Top three words that occurred the most: {}\n".format(topThree)

# -------------------------------------------------------------------

# Question 10
# Count the frequency of letters/numbers/symbols in a file.

def character_frequency(filename):
    with open(filename, "r") as foo:
        return Counter(foo.read())

filename = raw_input("What is your filename?")
chars = character_frequency(filename)
print "Keyborad Character Frequencies: {}".format(chars)
print "Number of spaces in file: ", chars[' '] #Can access elements. Accessing the number of spaces throughout the file.
print '\n'

# -------------------------------------------------------------------

# Question 11
# Count the frequency of equivalent lines in a file.

def line_frequency(filename):
    with open(filename, "r") as foo:
        return Counter(foo)

filename = raw_input("What is your filename?")
lineFreq = line_frequency(filename)
print "Line Frequencies: {}".format(lineFreq)
print '\n'

# -------------------------------------------------------------------

# Question 12
# Get the file size of a plain file.
def file_size(filename):
    try:
        with open(filename, "r") as foo:
            fileStats = os.stat(filename)
            #print fileStats
            return fileStats.st_size
    except IOError:
        print "{} does not exist! Enter a file that exists".format(filename)

filename = raw_input("What is your filename?")
print "Size of File: {}".format(file_size(filename))

# -------------------------------------------------------------------

# Question 13
# Write a list to a file.

# BECAREFUL.  If filename exists it will overwrite files contents. (Addressed in Q14)
# Use the append file permission instead if you wish to append the list at the end of a file.
def write_list(filename):
    with open(filename, "w+") as foo:
        list1 = ['this is line 1', 'this is line 2']
        for element in list1:
            foo.write(element)
        # element is a string, so add '\n' to get each list element printed out on a newline like this:
        # for element in list1:
        #    foo.write("{}\n".format(element))

filename = raw_input("Enter file name:")
write_list(filename)

# -------------------------------------------------------------------

# Question 14
# Write a program based on user input that either overwrites, appends to, or does nothing to a file.
# If the given file name doesn't exist, create it as a new file and write data to it.

def write_file(fname, perm):
    with open(fname, perm) as foo:
        #print foo.tell() If 'w+' then it is 0 as you are starting at the beginnning of the file.
        print "\nWrite your data to file {}".format(fname), "When finished type 'q' to quit the program:"
        loop = True
        while loop:
            userData = raw_input()
            if userData == 'q':
                break
            foo.write(str(userData) + "\n")

filename = raw_input("Enter file name:")
if os.path.isfile(filename) is True:
    decision = raw_input("\n{} already exists! You have 3 options:\n1) Overwrite the file.\n2) Append to the file.\n3) Do nothing and exit program.\n(To overwrite type 'o', to append type 'a', to exit hit any other key)".format(filename))
    if decision.lower() == 'o':
        write_file(filename, 'w+')
    elif decision.lower() == 'a':
        write_file(filename, 'a+')
    else:
        exit()
else:
    print "Creating new file named {}".format(filename)
    write_file(filename, 'w+')

# -------------------------------------------------------------------

# Question 15
# Copy the contents of a file to another file.
def copy_contents(originalFile, newFile):
    try:
        with open(originalFile) as originalCopy:
            with open(newFile, "w+") as newCopy:
                for line in originalCopy:
                    newCopy.write(line)
    except IOError:
        print "{} does not exist! Enter a file that exists".format(originalFile)

originalFile = raw_input("Enter the original file:")
newFile = raw_input("Enter the new file:")
copy_contents(originalFile, newFile)

# You can also use the shutil library to quickly copy a files contents to a new file.
# Make sure to have 'from shutil import copyfile' at the top of the program
copyfile(originalFile, newFile)

# -------------------------------------------------------------------

# Question 16
# Append a files contents to another file.

def append_to(originalFile, appendedToFile):
    try:
        with open(originalFile) as originalCopy:
            with open(appendedToFile, "a+") as appendedCopy:
                for line in originalCopy:
                    appendedCopy.write(line)
    except IOError:
        print "{} does not exist! Enter a file that exists".format(originalFile)

originalFile = raw_input("Name of original file: ")
appendedToFile = raw_input("Name of file to append original file's contents to: ")
append_to(originalFile, appendedToFile)


# -------------------------------------------------------------------

# Question 17
# Reverse contents of a file and write the result to a new file.

# Keep an eye on the file size. 'content = originalCopy.readlines()' loads all the file's data into a list in memory. Make sure there is enough free memory space.
# 'content.reverse()' is an in-place reversal. A new copy is not created, so no new memory space is allocated either. This can be more efficient and save memory space.

def reverse_file(originalFile, reverseFile):
    try:
        with open(originalFile, 'r') as originalCopy:
            with open(reverseFile, 'w+') as reverseCopy:
                content = originalCopy.readlines()
                content.reverse()
                for element in content:
                    reverseCopy.write(element.strip() + "\n")
    except IOError:
        print "{} does not exist! Enter a file that exists".format(originalFile)

originalFile = raw_input("File to copy contents of: ")
reverseFile = raw_input("File with contents of {} in reverse order: ".format(originalFile))
reverse_file(originalFile, reverseFile)

# -------------------------------------------------------------------

# Question 18
# Determine if a file is closed or not.

# Within the context manager the file is open.  We can confirm by calling foo.closed which will return False.  Outside the context manager the file is closed and foo.closed will return True
def is_closed(filename):
    try:
        with open(filename, 'r') as foo:
            print "Is {} closed ?: {}".format(filename, foo.closed)
        print "Is {} closed ?: {}".format(filename, foo.closed)
    except IOError:
        print "{} does not exist! Enter a file that exists".format(filename)

#filename = raw_input("Enter file name: ")
filename = 'test.txt'
is_closed(filename)

# -------------------------------------------------------------------

# Question 19
# Read a random line from a file.

def random_line(filename):
    try:
        with open(filename, 'r') as foo:
            lines = foo.read().splitlines()
            return random.choice(lines)
    except IOError:
        print "{} does not exist! Enter a file that exists".format(filename)
        return IOError

#filename = raw_input("Enter file name: ")
filename = 'test.txt'
value = random_line(filename)
if value != IOError:
    print "Random line from {}: ".format(filename), value

# -------------------------------------------------------------------
