# pdf-search

Searches for text in pdf but compared to a normal search like control + f this can go deeper and search from the search results 

## Example
Say you have a file hello.pdf with the lines

#hello.pdf
'''

hello world this is my first program

hello world this is my first piece of code written in c++
'''


with this program python3 search.py [filename] "hello" "world" "c++"

this will return "hello world this is my first piece of code written in c++" along with the line number in the pdf 

