import tkinter as tk

def main():
    
    #Create Root Window
    root = tk.Tk()
    
    #Root Window Title and Dimensions
    root.title("Welcome to Test")
    # Set Geometry (width x height)
    root.geometry('350x200')
    
    
    #all widgets here
    
    #adding a Label to Root Window
    lbl = tk.Label(root, text = "Are you testing?")
    #grid() function is a Geometry manager, no params = 0,0
    lbl.grid()
    
    def clicked():
        lbl.configure(text = "I just got clicked")
    
    btn = tk.Button(root, text = "Click me", fg = "red", command=clicked)
    
    btn.grid(column=1, row=0)
    
    #execute Tkinter
    root.mainloop()




if __name__ == "__main__":
    main()
