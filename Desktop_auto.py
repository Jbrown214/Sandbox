
import pywinauto
from pywinauto.application import Application
import time

nums = [x for x in range(1,52)]
p = 0

app = Application().start("notepad.exe")

app.Notepad.type_keys("^S")
app.SaveAs.edit1.set_edit_text("Test_File_demo.txt")
app.SaveAs.Save.click()

time.sleep(0.5)


while p < len(nums):
    app.Notepad.edit1.set_edit_text("test %r" % p)
    time.sleep(0.2)
    app.Notepad.type_keys("^S")
    # time.sleep(2)
    p += 1
    
