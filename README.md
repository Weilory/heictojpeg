# heictojpeg
convert HEIC to JPEG, for all HEIC files in current directory including its sub-directories. 

<hr />

### I/O

before running

```txt
homework
--- main.py
--- request.HEIC
--- snipshots
   --- image1.HEIC
   --- image2.HEIC
```

> `python heictojpg.py`

result

```
homework
--- main.py
--- request.HEIC
--- request.JPEG
--- snipshots
   --- image1.HEIC
   --- image2.HEIC
   --- image1.JPEG
   --- image2.JPEG
```

#### here if you call:

> `python undo.py`

result

```
homework
--- main.py
--- request.HEIC
--- snipshots
   --- image1.HEIC
   --- image2.HEIC
```

#### but if you call:

> `python clean.py`

result

```
homework
--- main.py
--- request.JPEG
--- snipshots
   --- image1.JPEG
   --- image2.JPEG
```

<hr >

### dependencies

```sh
pip install pyheif
pip install Pillow
```
