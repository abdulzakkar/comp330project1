# comp330project1

### 9/15/17
+ Today, we set up the github and cloud 9.
+ We added the sample notes files to the directory in cloud 9.

### 9/16/17
+ Today, we got Katie connected to the github through cloud9, and now both Abdul and Katie are collaborators in the project. 
+ Also, notes.py file now has one function which can report all the mentions present in each file.
+ The functionality was added into the file report_mentions.py, we will continue to separate different functions into individual py files.
+ To do:
+ The numbers correspond to the functions requested in the homework page:
1. is done
2. Abdul first
3. Katie first
4. Katie second
5. Abdul second
6. We'll see

### 9/18/17
+ Today, we decided to create a system for the user to control file input and output.
+ The notes.py program takes a directory argument in which all the notes are found.
+ The user can build an output from the program using available tools, each of which is written in a different py file.
+ If the user only wants to see the results of two tools, 
it is possible to select only those tools and quit out of the program to view the results.
+ We wrote the second tool, which is to organize notes by mention called organize_by_mention.py.
+ To do:
1. There are four remaining tools to build (3,4,5,6).
2. Consider improving format of output.
3. The output file can be placed in a location selected by the user, and named as per the user's liking.
4. We need to set up a Trello project and record communications and history through it.

### 9/19/17
+ Today, we set up the keyword collection system.
+ Keywords are words that appear in the set of notes at least 3 times.
+ Certain words are filtered out from becoming keywords (words like 'the' and 'of').
+ Such words are compiled and stored in boring_words_filtered.txt
+ To do:
1. Search for word tool
2. organize by keywords tool
3. topologically organize tool
4. improve UI

### 9/20/17
+ Today, we focused on a complete user interface overhaul. Everthing is streamlined, and most if not all errors are caught.
+ We set up a saving file interface with overwrite functionality and file naming.
+ We set up syntax for using certain tools.
+ Using tool C can take an integer for the number of columns to print with.
+ Using tool E can take an integer for the number of files necessary for a keyword to appear in its output.
+ To do:
1. Complete the term search function. Set up syntax just like tools C and E.
2. Work on tool F: topological sorting.
3. Work on documentation for the entire project.

### 9/21/17
+ Today, we worked on completing both the search terms tool (D) and the topological sort tool (F).
+ Tools C, D, and E all utilize the new syntax system for passing data to different tools manualy.
+ We fixed the potential for the save function to crash if the user does not properly answer yes or no questions.
+ To do:
1. Pyunit testing.
2. Documentation.
3. Proper file management.

