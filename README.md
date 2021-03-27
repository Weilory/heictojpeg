# heictojpg
convert HEIC to JPG, for all HEIC files in current directory including its sub-directories. 

<hr />

### I/O

before running

'''txt
homework
--- main.py
--- request.HEIC
--- snipshots
   --- image1.HEIC
   --- image2.HEIC
'''

'''py
python main.py
'''

result

'''txt
homework
--- main.py
--- request.jpg
--- snipshots
   --- image1.jpg
   --- image2.jpg
'''

<hr >

### notes

> This application does not modify image content, it simply rename `HEIC` file to `jpg`

