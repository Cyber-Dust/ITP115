Dasean Volk, dvolk@usc.edu

Fall 2021, ITP 115

Section: Boba

Week 11 Notes

# Files

:star: YOU CAN DO ALL OF THIS WITH PANDAS :star:

:star: For example: pd.read_csv('.csv') or pd.read_json('.json') :star:

* A file is a collection of information
* Stored as text (.py, .html, .css) or binary ([Word Doc] .docx, [Images] .jpg, .png, [Music] .mp3)

#### OPEN A FILE
* Use open()

`
file_obj = open(filename, mode)

fileIn = open("words.txt", "r")
`
* "r" = read or file access mode
* "words" = file name
* ".txt" = file type

 2 parameters to the function:
* **File Name** is a string variable for the name of the file
* **Mode** is a string variable for the file access mode "r"

Function returns: file_obj
* a **file object variable** (new variable type)

#### **CLOSE** A FILE
* Use close()

`
file_obj.close()
`
#### PROCESS CSV FILES

Take any data and saves it into CSV (Comma Seperated Values)

`
list = string.split(",")
`




#### **READ** HEADLINE

* Many CSV files have a header row to label each column
* To read the first line, can use the readline() method

`
string = file_obj.readline()
`

#### **WRITE** A FILE

2 parameters to the function:
* **File Name** is a string variable for the name of the file
* **Mode** is a string variable for the file access mode "w"

`
print(object(s), sep=separator, end=end, file=file_obj)

file_obj.close()
`
"r" 
* Read from a file.
* If the file doesn't exist, Python will generate an error.
"w"
* Write to a file.
* If the file exists, its contents are overwritten/replaced.
* If the file doesn't exist, it's created.
"a"
* Append a file.
* If the file exists, new data is appended to it.
* If the file doesn't exist, it's created.



