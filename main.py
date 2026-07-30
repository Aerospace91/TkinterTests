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
    
    #execute Tkinter
    root.mainloop()


if __name__ == "__main__":
    main()
