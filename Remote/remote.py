from tkinter import *
import tkinter as tk
import PIL
from PIL import ImageTk
from PIL import Image 

HEIGHT=900
WIDTH=900
root=tk.Tk()

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image=tk.PhotoImage(file='backgroun2.png')
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)


frame=tk.Frame(background_label,bg='grey')
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.6)


scale = Scale( frame,
              from_=0,
              to=10,
              length=500,
              orient=HORIZONTAL, #orientation of scale
              font = ('Consolas',20),
              tickinterval = 1, #adds numeric indicators for value
              #showvalue = 0, #hide current value
              resolution = 1, #increment of slider
              troughcolor = 'grey',
              fg = 'white',
              bg = '#111111'

              )
scale.set(((scale['from']-scale['to'])/2)+scale['to']) #set current value of slider

scale.pack(side='top')

frame2=Frame(frame,bg='darkgrey')
frame2.place(relx=0,rely=0.4,relwidth=0.45,relheight=0.6)

image1=tk.PhotoImage(file='up.png')
button=tk.Button(frame2,bg='gray',image=image1)
button.pack(side='top')    

image2=tk.PhotoImage(file='down.png')
button=tk.Button(frame2,bg='gray',image=image2)
button.pack(side='bottom') 

image3=tk.PhotoImage(file='right.png')
button=tk.Button(frame2,bg='gray',image=image3)
button.pack(side='right')

image4=tk.PhotoImage(file='left.png')
button=tk.Button(frame2,bg='gray',image=image4)
button.pack(side='left') 

frame3=Frame(frame,bg='darkgrey')
frame3.place(relx=0.5,rely=0.4,relwidth=0.5,relheight=0.6)


image5=tk.PhotoImage(file='anticlock.png')
button=tk.Button(frame3,bg='gray',image=image5)
button.pack(side='left') 


image6=tk.PhotoImage(file='clock.png')
button=tk.Button(frame3,bg='gray',image=image6)
button.pack(side='right') 

image7=tk.PhotoImage(file='start2.png')
button=tk.Button(frame3,bg='gray',image=image7)
button.pack(side='top') 

image8=tk.PhotoImage(file='stop-buttonpng.png')
button=tk.Button(frame3,bg='gray',image=image8)
button.pack(side='bottom') 


root.mainloop()