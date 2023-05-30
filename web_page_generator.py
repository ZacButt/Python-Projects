
import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width= 30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10) , pady=(10,10))

        # Create an entry widget to input custom text
        self.custom_text_entry = Entry(self.master, width=50)
        self.custom_text_entry.grid(row=1, column=0, padx=(10, 10), pady=(0, 10))
        
        # Create a button to generate web page with custom text
        self.custom_text_btn = Button(self.master, text="Generate Custom HTML Page", width=30, height=2, command=self.customHTML)
        self.custom_text_btn.grid(row=2, column=0, padx=(10, 10), pady=(0, 10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "<h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        htmlText = self.custom_text_entry.get()
        htmlFile = open("custom.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "<h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("custom.html")
                 



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
