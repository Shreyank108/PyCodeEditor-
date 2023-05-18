from tkinter import *
from tkinter.filedialog import asksaveasfilename ,askopenfilename
import pyttsx3
import subprocess 

engine=pyttsx3.init() 
voices=engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def talk(text): 
    engine.say(text) 
    engine.runAndWait()

compiler=Tk() 
compiler.title("Shreyank's Code Editor")
talk("Opening the shreyank's Code Editor")

file_path=''

def set_file_path(path): 
    global file_path 
    file_path=path 
     
def open_file():
    path=askopenfilename(filetypes=[('python files','*.py')]) 
    with open (path,'r')as file : 
        code=file.read() 
        editor.delete('1.0',END)
        editor.insert('1.0',code) 
        set_file_path(path)
        
def saveas():
    if file_path == '':
        path=asksaveasfilename(filetypes=[('python files','*.py')]) 
    else : 
        path=file_path
    with open (path,'w')as file : 
         code=editor.get('1.0',END) 
         file.write(code)
         set_file_path(path)
         
def run():
   command=f'python {file_path} '
   process=subprocess.Popen(command,stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE ,
                            shell=True)
   output , error = process.communicate() 
   code_output.insert('1.0',output)
   code_output.insert('1.0',error)
  
   
def for_loop(): 
    editor.insert(" for i in range () ")
    

       
menu_button=Menu(compiler) 
    
file_menu=Menu(menu_button,tearoff=0) 
file_menu.add_command(label="Open",command=open_file) 
file_menu.add_command(label="Save",command=saveas) 
file_menu.add_command(label="Save As",command=saveas) 
file_menu.add_command(label="Exit",command=exit) 
menu_button.add_cascade(label="FILE",menu=file_menu)

run_button=Menu(menu_button,tearoff=0) 
run_button.add_command(label="OH YEAH",command=run) 
menu_button.add_cascade(label="RUN",menu=run_button) 

snippet=Menu(menu_button,tearoff=0) 
snippet.add_command(label="class",command=run) 
menu_button.add_cascade(label="while loop",command=run)
snippet.add_command(label="for loop",command=for_loop) 
menu_button.add_cascade(label="snipet",menu=snippet) 

compiler.config(menu=menu_button) 

editor=Text(bg="pink",foreground="black",border=10,width=500,height=20,font=(5)) 
editor.pack()

code_output=Text(bg="black",foreground="white",border=10,height=25,width=500,font=5) 
code_output.pack()


compiler.mainloop()

