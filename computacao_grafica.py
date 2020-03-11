from tkinter import *

canvas_width = 500
canvas_height = 500

telinha = Tk()
telinha.title("casinha")
w = Canvas(telinha, width=canvas_width,height=canvas_height)
w.pack(expand = YES,fill=BOTH)
#criacao dos eixos
w.create_line(10,10,10,490)#eixo y
w.create_line(10,490,490,490)#eixo x
#parte de baixo da casa
w.create_rectangle(40,465,40,465,fill='black',width = 2)#ponto mas proximo da origem
w.create_rectangle(80,465,80,465,fill='black',width = 2)#ponto da direita da origem
w.create_line(40,465,80,465)
#parede esquerda0
w.create_rectangle(40,435,40,435,fill='black',width = 2)#ponto em cima da origem
w.create_line(40,465,40,435)
#telhado parte esquerda
w.create_rectangle(20,435,20,435,fill='black',width = 2)#ponto a esquerda do ponto em cima da origem
w.create_line(40,435,20,435)
w.create_rectangle(40,415,40,415,fill='black',width = 2)#segundo ponto a cima da origem
w.create_line(20,435,40,415)
#chamine
w.create_rectangle(50,415,50,415,fill='black',width = 2)#ponto de baixo da chamine|esquerdo|
w.create_line(50,415,40,415)
w.create_rectangle(50,400,50,400,fill='black',width = 2)#ponto de cima da chamine|esquerdo|
w.create_line(50,415,50,400)
w.create_rectangle(60,400,60,400,fill='black',width = 2)#ponto de cima da chamine|direito|
w.create_line(50,400,60,400)
w.create_rectangle(60,415,60,415,fill='black',width = 2)#ponto de baixo da chamine|direito|
w.create_line(60,400,60,415)
#teto
w.create_rectangle(80,415,80,415,fill='black',width = 2)#ponto da direita do teto
w.create_line(60,415,80,415)
w.create_rectangle(100,435,100,435,fill='black',width = 2)#ponto mais a direita do teto
w.create_line(80,415,100,435)
w.create_rectangle(80,435,80,435,fill='black',width = 2)#parede da direita|cima|
w.create_line(80,435,100,435)
w.create_line(80,435,80,465)
telinha.mainloop()
