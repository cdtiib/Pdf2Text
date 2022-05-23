import re
import time
from tkinter import Tk

cache = ""

while True:
    try:
        data = Tk().clipboard_get()
        if data != cache:
            # remove too many spaces (more than 1)
            string = re.sub(r'\s+', ' ', data)
            # remove line breaks
            string = re.sub(r'\n', ' ', string)
            # capitalize first letter
            string = string[0].upper() + string[1:]
            print(string)

            cache = Tk().clipboard_get()
    except Exception:
        pass
    time.sleep(1)
