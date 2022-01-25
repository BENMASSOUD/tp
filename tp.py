Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import threading, time
>>> def run_thread(self, name, delay ):
print ("Process " + name + " starting.")
for idx in range (5):
print(name + " Working")
time.sleep(delay)
print ("Process " + name + " finished.")
SyntaxError: expected an indented block
>>> 