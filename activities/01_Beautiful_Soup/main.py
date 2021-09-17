import os
from bs4 import BeautifulSoup

data_folder = "data_files"

TXT_FILE  = os.path.join(data_folder, "file.txt")
CSV_FILE  = os.path.join(data_folder, "file.csv")
XML_FILE  = os.path.join(data_folder, "file.xml")
HTML_FILE = os.path.join(data_folder, "file.html")
JSON_FILE = os.path.join(data_folder, "file.json")


def read_file(filepath):
    if not os.path.exists(filepath):
        print("File not found:  " + filepath)
        quit()
    else:
        return open(filepath, "r")


def examine(variable):
    print("\n", variable, "\n")
    print("    ## object type: ", type(variable), "\n")
    quit()


def print_list(list):
    count = 0
    newline = "        #   "
    for x in list:
        y = repr(x).replace('\n', '\n' + newline + "      ")
        print(f"{newline}[{count}]:  {y}")
        count += 1

    print("    ## object type: ", type(list), " of ", type(x))

    # type1 = str(type(list))[8:-2]
    # type2 = str(type(x))[8:-2]
    # print("\n    ## object type:", type1, "of", type2)


    quit()


if __name__ == "__main__":

    file = read_file(HTML_FILE)
    ## print(file)   →   <_io.TextIOWrapper name='data_files\\file.html' mode='r' encoding='cp1252'>
    ## object type:  _io.TextIOWrapper

    var = file.read()
    ## returns text identical to the original file, including whitespace
    ## object type:  <class 'str'>


    file = read_file(HTML_FILE)
    soup = BeautifulSoup(file, "html.parser")
    ## returns text identical to the original file but with no whitespace
    ## except that it ADDS a linebreak after <!DOCTYPE html> for some reason....
    ## object type:  <class 'bs4.BeautifulSoup'>


    var = soup.prettify()
    ## returns formatted html/xml with 1-space indents and every <element> and </element> tag on a newline
    ## it doesn't add an extra space after <!DOCTYPE>
    ## object type:  <class 'str'>


    var = soup.p
    ## soup.ELEMENT   →   returns the first <element> AND everything contained inside
    ## print(var)     →   <p class="title class2"><b><i>The Dormouse's story</i></b></p>
    ## object type:  <class 'bs4.element.Tag'>


    var = soup.title.name
    ## TAG.name   →   returns the name of the outer element in the tag
    ## print(var) →   title
    ## object type:  <class 'str'>


    var = soup.p.string
    ## TAG.string   →   returns the text contained within the tag
    ## print(var)   →   The Dormouse's story
    ## only works if there is ONE descendant string.
    ## object type:  <class 'bs4.element.NavigableString'>


    var = soup.body.stripped_strings
    ## TAG.stripped_strings   →   returns the text contained within the tags as a Generator
    ## output AFTER converting to list:
        #   [0]:  The Dormouse's story
        #   [1]:  Once upon a time there were three little sisters; and their names were
        #   [2]:  Elsie
        #   [3]:  ,
        #   [4]:  Lacie
        #   [5]:  and
        #   [6]:  Tillie
        #   [7]:  ;\nand they lived at the bottom of a well.
        #   [8]:  ...
    ## object type:  <class 'generator'>  of  <class 'str'>


    var = soup.title.parent.name
    ## TAG.parent.name   →   returns the element name of the tag's immediate parent
    ## print(var)        →   head
    ## object type:  <class 'str'>


    var = (soup.p['class'])
    ## TAG['attribute'] returns the attributes of the tag as a list:
        #   [0]:  'title'
        #   [1]:  'class2'
    ## object type:  <class 'list'>  of  <class 'str'>


    var = soup.find_all('a')
    ## soup.find_all(ELEMENT)   →   returns a ResultSet with all elements in the file
        #   [0]:  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
        #   [1]:  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
        #   [2]:  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    ## object type:  <class 'bs4.element.ResultSet'>  of  <class 'bs4.element.Tag'>


    var = soup.find_all('a')[0]
    ## soup.find_all(ELEMENT)[0]   →   returns the tag of the first item in the ResultSet
    ## print(var)                  →   <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    ## object type:  <class 'bs4.element.Tag'>


    var = soup.get_text()
    ## print(var)   →
        ##      < 4 blank lines >
        ## The Dormouse's story
        ##      < 2 blank lines >
        ## The Dormouse's story
        ## Once upon a time there were three little sisters; and their names were
        ## Elsie,
        ## Lacie and
        ## Tillie;
        ## and they lived at the bottom of a well.
        ## ...
    ## object type:  <class 'str'>


    var = soup.body.children
    ## TAG.children   →   returns interior tags as a list ITERATOR (linked list; no index)
    ## output AFTER converting to list:
    #   [0]:  '\n'
    #   [1]:  <p class="title class2"><b><i>The Dormouse's story</i></b></p>
    #   [2]:  '\n'
    #   [3]:  <p class="story">Once upon a time there were three little sisters; and their names were
    #         <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #         <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
    #         <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
    #         and they lived at the bottom of a well.</p>
    #   [4]:  '\n'
    #   [5]:  <p class="story">...</p>
    #   [6]:  '\n'
    ## object type:  <class 'list_iterator'>  of  <class 'bs4.element.NavigableString'>

    var = soup.body.contents
    ## TAG.children   →   returns interior tags as a list
    #   [0]:  '\n'
    #   [1]:  <p class="title class2"><b><i>The Dormouse's story</i></b></p>
    #   [2]:  '\n'
    #   [3]:  <p class="story">Once upon a time there were three little sisters; and their names were
    #         <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #         <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
    #         <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
    #         and they lived at the bottom of a well.</p>
    #   [4]:  '\n'
    #   [5]:  <p class="story">...</p>
    #   [6]:  '\n'
    ## object type:  <class 'list'>  of  <class 'bs4.element.NavigableString'>


    var = soup.body.descendants
    ## TAG.descendants   →   returns ALL* interior tags as a 'generator' object
    ## nested tags will be returned multiple times  (see lines 1-4)
    ## output AFTER converting to list:
    #   [0]:  '\n'
    #   [1]:  <p class="title class2"><b><i>The Dormouse's story</i></b></p>
    #   [2]:  <b><i>The Dormouse's story</i></b>
    #   [3]:  <i>The Dormouse's story</i>
    #   [4]:  "The Dormouse's story"
    #   [5]:  '\n'
    #   [6]:  <p class="story">Once upon a time there were three little sisters; and their names were
    #         <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #         <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
    #         <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
    #         and they lived at the bottom of a well.</p>
    #   [7]:  'Once upon a time there were three little sisters; and their names were\n'
    #   [8]:  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    #   [9]:  'Elsie'
    #   [10]:  ',\n'
    #   [11]:  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    #   [12]:  'Lacie'
    #   [13]:  ' and\n'
    #   [14]:  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    #   [15]:  'Tillie'
    #   [16]:  ';\nand they lived at the bottom of a well.'
    #   [17]:  '\n'
    #   [18]:  <p class="story">...</p>
    #   [19]:  '...'
    #   [20]:  '\n'
    ## object type:  <class 'generator'>  of  <class 'bs4.element.NavigableString'>


# .parent        the tag's immediate parent tag
# .parents       all the parent tags
# .contents      strings and tags one step inside as a LIST
# .children      strings and tags one step inside as an ITERABLE
# .descendants   all strings and tags inside as a GENERATOR
# .siblings      all tags at the same level within the same parent

# .next_sibling
# .previous_sibling

# .next_siblings
# .previous_siblings

# .next_element
# .previous_element

# .next_elements
# .previous_elements


    var = soup.children
    print_list(var)
    examine(var)

