Dasean Volk, dvolk@usc.edu
Fall 2021, ITP 115
Section: Boba
Week 11 Notes

# Files

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
* **Mode** is a string variable for the file access mode

Function returns: file_obj
* a **file object variable** (new variable type)

#### **CLOSE** A FILE
* Use close()

`
file_obj.close()
`

Take any data and saves it into CSV (Comma Seperated Values)
`
def main():
fin = open("names.txt", "r")
for line in fin:
line = line.strip()
name = line.split(" ")
first_name = name[0]
last_name = name[1]
print(last_name + ", " + first_name)
fin.close()
main()
`

#### **READ** A FILE


#### **WRITE** A FILE

