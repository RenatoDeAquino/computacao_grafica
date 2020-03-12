from tkinter import *
#variaveis
canvas_width = 500
canvas_height = 500


telinha = Tk()
telinha.title("casinha")
w = Canvas(telinha, width=canvas_width,height=canvas_height)
w.pack(expand = YES,fill=BOTH)
#criacao dos eixos
w.create_line(250,0,250,500)
w.create_line(0,250,500,250)
#---------------------------
point_1  = [270,230]#20|20
point_2  = [270,220]#20|30
point_3  = [260,220]#10|30
point_4  = [270,210]#20|40
point_5  = [275,210]#25|40
point_6  = [275,205]#25|45
point_7  = [280,205]#30|45
point_8  = [280,210]#30|40
point_9  = [290,210]#40|40
point_10 = [300,220]#50|30
point_11 = [290,220]#40|30
point_12 = [290,230]#40|20

#---------------------------não mexer na parte de baixo
#pontos
w.create_rectangle(point_1 [0],point_1 [1],point_1 [0],point_1 [1],fill='black',width=2)
w.create_rectangle(point_2 [0],point_2 [1],point_2 [0],point_2 [1],fill='black',width=2)
w.create_rectangle(point_3 [0],point_3 [1],point_3 [0],point_3 [1],fill='black',width=2)
w.create_rectangle(point_4 [0],point_4 [1],point_4 [0],point_4 [1],fill='black',width=2)
w.create_rectangle(point_5 [0],point_5 [1],point_5 [0],point_5 [1],fill='black',width=2)
w.create_rectangle(point_6 [0],point_6 [1],point_6 [0],point_6 [1],fill='black',width=2)
w.create_rectangle(point_7 [0],point_7 [1],point_7 [0],point_7 [1],fill='black',width=2)
w.create_rectangle(point_8 [0],point_8 [1],point_8 [0],point_8 [1],fill='black',width=2)
w.create_rectangle(point_9 [0],point_9 [1],point_9 [0],point_9 [1],fill='black',width=2)
w.create_rectangle(point_10[0],point_10[1],point_10[0],point_10[1],fill='black',width=2)
w.create_rectangle(point_11[0],point_11[1],point_11[0],point_11[1],fill='black',width=2)
w.create_rectangle(point_12[0],point_12[1],point_12[0],point_12[1],fill='black',width=2)
#---------------------------não mexer na parte de baixo nem na de cima
#retas
w.create_line(point_1 [0],point_1 [1],point_2 [0],point_2 [1])
w.create_line(point_2 [0],point_2 [1],point_3 [0],point_3 [1])
w.create_line(point_3 [0],point_3 [1],point_4 [0],point_4 [1])
w.create_line(point_4 [0],point_4 [1],point_5 [0],point_5 [1])
w.create_line(point_5 [0],point_5 [1],point_6 [0],point_6 [1])
w.create_line(point_6 [0],point_6 [1],point_7 [0],point_7 [1])
w.create_line(point_7 [0],point_7 [1],point_8 [0],point_8 [1])
w.create_line(point_8 [0],point_8 [1],point_9 [0],point_9 [1])
w.create_line(point_9 [0],point_9 [1],point_10[0],point_10[1])
w.create_line(point_10[0],point_10[1],point_11[0],point_11[1])
w.create_line(point_11[0],point_11[1],point_12[0],point_12[1])
w.create_line(point_12[0],point_12[1],point_1 [0],point_1 [1])
#--------------------------não mexer na parte de cima
menu = int(input("1-transladar \n2-escalar\n3-espelhar"))
if menu == 1:
    ajudax = float(input("Digite o quanto quer andar no eixo x"))
    ajuday = float(input("Digite o quanto quer andar no eixo y"))
    point_1 [0] += ajudax
    point_2 [0] += ajudax
    point_3 [0] += ajudax
    point_4 [0] += ajudax
    point_5 [0] += ajudax
    point_6 [0] += ajudax
    point_7 [0] += ajudax
    point_8 [0] += ajudax
    point_9 [0] += ajudax
    point_10[0] += ajudax
    point_11[0] += ajudax
    point_12[0] += ajudax
    #---------------------
    point_1 [1] -= ajuday
    point_2 [1] -= ajuday
    point_3 [1] -= ajuday
    point_4 [1] -= ajuday
    point_5 [1] -= ajuday
    point_6 [1] -= ajuday
    point_7 [1] -= ajuday
    point_8 [1] -= ajuday
    point_9 [1] -= ajuday
    point_10[1] -= ajuday
    point_11[1] -= ajuday
    point_12[1] -= ajuday
    w.delete('all')
    w.create_line(250,0,250,500)
    w.create_line(0,250,500,250)
    w.create_line(point_1 [0],point_1 [1],point_2 [0],point_2 [1])
    w.create_line(point_2 [0],point_2 [1],point_3 [0],point_3 [1])
    w.create_line(point_3 [0],point_3 [1],point_4 [0],point_4 [1])
    w.create_line(point_4 [0],point_4 [1],point_5 [0],point_5 [1])
    w.create_line(point_5 [0],point_5 [1],point_6 [0],point_6 [1])
    w.create_line(point_6 [0],point_6 [1],point_7 [0],point_7 [1])
    w.create_line(point_7 [0],point_7 [1],point_8 [0],point_8 [1])
    w.create_line(point_8 [0],point_8 [1],point_9 [0],point_9 [1])
    w.create_line(point_9 [0],point_9 [1],point_10[0],point_10[1])
    w.create_line(point_10[0],point_10[1],point_11[0],point_11[1])
    w.create_line(point_11[0],point_11[1],point_12[0],point_12[1])
    w.create_line(point_12[0],point_12[1],point_1 [0],point_1 [1])
if menu == 2:
    ajudax = float(input("quer escalar pra quanto no x"))
    ajuday = float(input("quer escalar pra quanto no y"))
    if ajudax > 0:
        point_7 [0] += ajudax
        point_8 [0] += ajudax
        point_9 [0] += ajudax
        point_10[0] += ajudax
        point_11[0] += ajudax
        point_12[0] += ajudax
    elif ajudax < 0:
        point_1 [0] += ajudax
        point_2 [0] += ajudax
        point_3 [0] += ajudax
        point_4 [0] += ajudax
        point_5 [0] += ajudax
        point_6 [0] += ajudax
        point_7 [0] += ajudax
        point_8 [0] += ajudax
    if ajuday > 0:
        point_2 [1] -= ajuday
        point_3 [1] -= ajuday
        point_4 [1] -= ajuday
        point_5 [1] -= ajuday
        point_6 [1] -= ajuday
        point_7 [1] -= ajuday
        point_8 [1] -= ajuday
        point_9 [1] -= ajuday
        point_10[1] -= ajuday
        point_11[1] -= ajuday
    elif ajuday < 0:
        point_1 [1] -= ajuday
        point_2 [1] -= ajuday
        point_3 [1] -= ajuday
        point_10[1] -= ajuday
        point_11[1] -= ajuday
        point_12[1] -= ajuday
    w.delete('all')
    w.create_line(250,0,250,500)
    w.create_line(0,250,500,250)
    w.create_line(point_1 [0],point_1 [1],point_2 [0],point_2 [1])
    w.create_line(point_2 [0],point_2 [1],point_3 [0],point_3 [1])
    w.create_line(point_3 [0],point_3 [1],point_4 [0],point_4 [1])
    w.create_line(point_4 [0],point_4 [1],point_5 [0],point_5 [1])
    w.create_line(point_5 [0],point_5 [1],point_6 [0],point_6 [1])
    w.create_line(point_6 [0],point_6 [1],point_7 [0],point_7 [1])
    w.create_line(point_7 [0],point_7 [1],point_8 [0],point_8 [1])
    w.create_line(point_8 [0],point_8 [1],point_9 [0],point_9 [1])
    w.create_line(point_9 [0],point_9 [1],point_10[0],point_10[1])
    w.create_line(point_10[0],point_10[1],point_11[0],point_11[1])
    w.create_line(point_11[0],point_11[1],point_12[0],point_12[1])
    w.create_line(point_12[0],point_12[1],point_1 [0],point_1 [1])
if menu == 3:
    ajudax = int(input("deseja espelhar no x?\n0 ou 1"))
    ajuday = int(input("deseja espelhar no y?\n0 ou 1"))
    if ajudax == 1:
        point_1 [0] -= 40  
        point_2 [0] -= 40
        point_3 [0] -= 20
        point_4 [0] -= 40
        point_5 [0] -= 50
        point_6 [0] -= 50
        point_7 [0] -= 60
        point_8 [0] -= 60
        point_9 [0] -= 80
        point_10[0] -= 100
        point_11[0] -= 80
        point_12[0] -= 80
    if ajuday == 1:
        point_1 [1] += 40  
        point_2 [1] += 60
        point_3 [1] += 60
        point_4 [1] += 80
        point_5 [1] += 80
        point_6 [1] += 90
        point_7 [1] += 90
        point_8 [1] += 80
        point_9 [1] += 80
        point_10[1] += 60
        point_11[1] += 60
        point_12[1] += 40


    
    w.delete('all')
    w.create_line(250,0,250,500)
    w.create_line(0,250,500,250)
    w.create_line(point_1 [0],point_1 [1],point_2 [0],point_2 [1])
    w.create_line(point_2 [0],point_2 [1],point_3 [0],point_3 [1])
    w.create_line(point_3 [0],point_3 [1],point_4 [0],point_4 [1])
    w.create_line(point_4 [0],point_4 [1],point_5 [0],point_5 [1])
    w.create_line(point_5 [0],point_5 [1],point_6 [0],point_6 [1])
    w.create_line(point_6 [0],point_6 [1],point_7 [0],point_7 [1])
    w.create_line(point_7 [0],point_7 [1],point_8 [0],point_8 [1])
    w.create_line(point_8 [0],point_8 [1],point_9 [0],point_9 [1])
    w.create_line(point_9 [0],point_9 [1],point_10[0],point_10[1])
    w.create_line(point_10[0],point_10[1],point_11[0],point_11[1])
    w.create_line(point_11[0],point_11[1],point_12[0],point_12[1])
    w.create_line(point_12[0],point_12[1],point_1 [0],point_1 [1])
    
telinha.mainloop()
