from tkinter import *
from tkinter import ttk
import googletrans
from googletrans import Translator
 
 
def translate_text():
    source_lang = source_lang_combo.get()
    target_lang = target_lang_combo.get()
    input_text = input_text_widget.get("1.0","end-1c")
 
 
    if not input_text:
        output_text_widget.delete("1.0","end")
 
 
    else:
        translator = Translator()
        translated_text = translator.translate(input_text,src=source_lang, dest=target_lang)
        output_text_widget.delete("1.0","end")
        output_text_widget.insert("1.0",translated_text.text)
 
 
#Create the main window
root = Tk()
root.title("Google Translator - The Pycodes")
root.geometry("1080x400")
root.resizable(False,False)
 
 
#source language combobox
source_lang_combo = ttk.Combobox(root,values=list(googletrans.LANGUAGES.values()),font="Roboto 14")
source_lang_combo.place(x=110,y=20)
source_lang_combo.set("English")
 
 
#target language combobox
target_lang_combo = ttk.Combobox(root,values=list(googletrans.LANGUAGES.values()),font="Roboto 14")
target_lang_combo.place(x=730,y=20)
target_lang_combo.set("Arabic")
 
 
#input text widget with scrollbar
input_text_frame = Frame(root, bd=5)
input_text_frame.place(x=10,y=118,width=440,height=210)
 
 
input_text_widget = Text(input_text_frame,font="Roboto 20", bg="white",relief=GROOVE, wrap=WORD)
input_text_widget.place(x=0,y=0,width=430,height=200)
 
 
input_text_scrollbar = ttk.Scrollbar(input_text_frame,orient="vertical", command=input_text_widget.yview)
input_text_scrollbar.pack(side="right",fill="y")
 
 
input_text_scrollbar.configure(command=input_text_widget.yview)
input_text_widget.configure(yscrollcommand=input_text_scrollbar.set)
 
 
#output text widget with scrollbar
output_text_frame = Frame(root,bd=5)
output_text_frame.place(x=620, y=118, width=440, height=210)
 
 
output_text_widget = Text(output_text_frame,font="Roboto 20", bg="white",relief=GROOVE, wrap=WORD)
output_text_widget.place(x=0,y=0,width=430,height=200)
 
 
output_text_scrollbar = ttk.Scrollbar(output_text_frame,orient="vertical", command=output_text_widget.yview)
output_text_scrollbar.pack(side="right",fill="y")
 
 
output_text_scrollbar.configure(command=output_text_widget.yview)
output_text_widget.configure(yscrollcommand=output_text_scrollbar.set)
 
 
#translate button
translate_button = Button(root,text="Translate",font="Roboto 15 italic",activebackground="green",
cursor="hand2",bd=5, bg="orange",fg="white",command=translate_text)
translate_button.place(x=475,y=250)
 
 
#adding image and icon
opposite_image = PhotoImage(file="opposite.png")
image_label = Label(root,image=opposite_image,width=150)
image_label.place(x=450,y=20)
 
 
image_icon = PhotoImage(file="translation.png")
root.iconphoto(False,image_icon)
 
 
root.mainloop()
