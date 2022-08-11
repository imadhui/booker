import clipboard as cb
import validators as vs
import os

# Say yes when a clipboard item contains a book link

msg = cb.paste()

def hasBookSuffix(s):
    if (s.endswith('pdf') or s.endswith('epub') or s.endswith('mobi')):
        return True
    else:
        return False

def isBookLink(s):
    if (vs.url(s) and hasBookSuffix(s)):
        print("Book")
        return True
    else:
        print("Not a Book")
        return False

# Step1: get name of the book
# Step2: Download it.

def downloadBook(url):
    command = f"wget {url}"
    os.system(command)

if (isBookLink(msg)):
    downloadBook(msg)
