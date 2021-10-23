from turtle import *
from random import *
import turtle
import time

#código para configuração da janela e detalhes estéticos importado de:
#https://www.youtube.com/watch?v=tXH-cY7N5bg
#tendo como base um monitor de 1920x1080 onde 1920 = número de linhas verticais
#temos que a velocidade = linhas verticais/ número de loops


#setup da janela
window = turtle.Screen()
window.title("corrida")
window.bgcolor("green")
turtle.speed(0)
turtle.penup()
window.setup(width = 1.0, height = 1.0)
turtle.hideturtle()

#titulo
titulo = turtle.Turtle()
titulo.penup()
titulo.speed(100)
titulo.hideturtle()
titulo.setpos(-100, 400)
titulo.write("Corrida", font=("Arial", 40, "bold"))

#terra
turtle.setpos(-900, 380)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(1700)
turtle.right(90)
turtle.forward(840)
turtle.right(90)
turtle.forward(1700)
turtle.right(90)
turtle.forward(840)
turtle.end_fill()

#Linha de Chegada
gap_size = 20
shape("square")
penup()
color("white")
for i in range(21):
    goto(770, (350 - (i * gap_size * 2)))
    stamp()
for i in range(21):
    goto(770 + gap_size, ((390 - gap_size) - (i * gap_size * 2)))
    stamp()
color("black")
for i in range(21):
    goto(770, (370 - (i * gap_size * 2)))
    stamp()
for i in range(21):
    goto(770 + gap_size, ((370 - gap_size) - (i * gap_size * 2)))
    stamp()

#tartaruga especial para escrever Vi na tela
tartaruga_v2 = Turtle()
tartaruga_v2.speed(100)
tartaruga_v2.hideturtle()
tartaruga_v2.penup()
tartaruga_v2.goto(-950, 400)

#tartaruga azul
tartaruga_azul = Turtle()
tartaruga_azul.speed(100)
tartaruga_azul.color("cyan")
tartaruga_azul.shape("turtle")
tartaruga_azul.hideturtle()
tartaruga_azul.shapesize(3.8)
tartaruga_azul.penup()
tartaruga_azul.goto(-800, 300)
acel_azul = 0
Vo_azul = 0
#tartaruga azul velocimetro
tartaruga_azul_v = Turtle()
tartaruga_azul_v.speed(100)
tartaruga_azul_v.hideturtle()
tartaruga_azul_v.penup()
tartaruga_azul_v.goto(-900, 300)



#tartaruga amarela
tartaruga_amarela = Turtle()
tartaruga_amarela.speed(100)
tartaruga_amarela.color("yellow")
tartaruga_amarela.shape("turtle")
tartaruga_amarela.hideturtle()
tartaruga_amarela.shapesize(3.8)
tartaruga_amarela.penup()
tartaruga_amarela.goto(-800, 100)
acel_amarelo = 0
Vo_amarelo = 0
#tartaruga amarela velocimetro
tartaruga_amarela_v = Turtle()
tartaruga_amarela_v.speed(100)
tartaruga_amarela_v.hideturtle()
tartaruga_amarela_v.penup()
tartaruga_amarela_v.goto(-900, 100)

#tartaruga laranja
tartaruga_laranja = Turtle()
tartaruga_laranja.speed(100)
tartaruga_laranja.color("orange")
tartaruga_laranja.shape("turtle")
tartaruga_laranja.hideturtle()
tartaruga_laranja.penup()
tartaruga_laranja.shapesize(3.8)
tartaruga_laranja.goto(-800, -100)
acel_laranja = 0
Vo_laranja = 0
#tartaruga laranja velocimetro
tartaruga_laranja_v = Turtle()
tartaruga_laranja_v.speed(100)
tartaruga_laranja_v.hideturtle()
tartaruga_laranja_v.penup()
tartaruga_laranja_v.goto(-900, -100)

#tartaruga rosa
tartaruga_rosa = Turtle()
tartaruga_rosa.speed(100)
tartaruga_rosa.hideturtle()
tartaruga_rosa.color("pink")
tartaruga_rosa.shape("turtle")
tartaruga_rosa.penup()
tartaruga_rosa.shapesize(3.8)
tartaruga_rosa.goto(-800, -300)
acel_rosa = 0
Vo_rosa = 0
#tartaruga rosa velocimetro
tartaruga_rosa_v = Turtle()
tartaruga_rosa_v.speed(100)
tartaruga_rosa_v.hideturtle()
tartaruga_rosa_v.penup()
tartaruga_rosa_v.goto(-900, -300)

#tartaruga que mostra o tempo
tartaruga_tempo = Turtle()
tartaruga_tempo.speed(100)
tartaruga_tempo.hideturtle()
tartaruga_tempo.penup()
tartaruga_tempo.goto(-850, 400)


#tartaruga que mostra o vencedor
tartaruga_titulo = Turtle()
tartaruga_titulo.speed(100)
tartaruga_titulo.hideturtle()
tartaruga_titulo.penup()
tartaruga_titulo.goto(-200, 0)
tartaruga_titulo.color("white")



#reunindo informações e alocando os vetores
qntd_tartarugas = turtle.textinput("","digite o número de tartarugas")
qntd_tartarugas = int(qntd_tartarugas)

acel_tartarugas = [0 for i in range(qntd_tartarugas)]
Vo_tartarugas = [0 for i in range(qntd_tartarugas)]
for i in range(qntd_tartarugas):
    acel_tartarugas[i] = float(turtle.textinput("aceleração tartaruga:",i+1))
    Vo_tartarugas[i] = float(turtle.textinput("Vo tartaruga:",i+1))

#Seleciona o número de tartarugas
if(qntd_tartarugas>= 1):
    tartaruga_azul.showturtle()
    tartaruga_azul.pendown()

    tartaruga_v2.write("Tempo=", font=("", 20))
    tartaruga_v2.goto(-950, 300)

    tartaruga_v2.write("V1=", font=("", 20))

    acel_azul = acel_tartarugas[0]
    Vo_azul = Vo_tartarugas[0]

    if(qntd_tartarugas >=2):
        tartaruga_amarela.showturtle()
        tartaruga_amarela.pendown()

        tartaruga_v2.goto(-950, 100)
        tartaruga_v2.write("V2=", font=("", 20))

        acel_amarelo = acel_tartarugas[1]
        Vo_amarelo = Vo_tartarugas[1]

        if(qntd_tartarugas>= 3):
            tartaruga_laranja.showturtle()
            tartaruga_laranja.pendown()

            tartaruga_v2.goto(-950, -100)
            tartaruga_v2.write("V3=", font=("", 20))
            
            acel_laranja = acel_tartarugas[2]
            Vo_laranja = Vo_tartarugas[2]
            
            if(qntd_tartarugas == 4):
                tartaruga_rosa.showturtle()
                tartaruga_rosa.pendown()

                tartaruga_v2.goto(-950, -300)
                tartaruga_v2.write("V4=", font=("", 20))

                acel_rosa = acel_tartarugas[3]
                Vo_rosa = Vo_tartarugas[3]

Num_loops = 0
#Faz a corrida
while tartaruga_azul.xcor() <= 765 and tartaruga_amarela.xcor() <= 765 and tartaruga_rosa.xcor() <= 765 and tartaruga_laranja.xcor() <= 765:
    #calcula a velocidade
    velocidade_azul =  Vo_azul + (acel_azul*Num_loops)
    velocidade_amarelo = Vo_amarelo +(acel_amarelo*Num_loops)
    velocidade_rosa = Vo_rosa + (acel_rosa*Num_loops) 
    velocidade_laranja = Vo_laranja + (acel_laranja*Num_loops)

    #mostra o velocimetro e o tempo
    if(qntd_tartarugas >= 1):
        tartaruga_azul_v.clear()
        tartaruga_azul_v.write(velocidade_azul, font= ("", 20))
        
        tartaruga_tempo.clear()
        tartaruga_tempo.write(Num_loops, font= ("", 20))

        if(qntd_tartarugas >=2):
            tartaruga_amarela_v.clear()
            tartaruga_amarela_v.write(velocidade_amarelo, font= ("", 20))

            if(qntd_tartarugas >= 3):
                tartaruga_laranja_v.clear()
                tartaruga_laranja_v.write(velocidade_laranja, font=("", 20))

                if(qntd_tartarugas == 4):
                    tartaruga_rosa_v.clear()
                    tartaruga_rosa_v.write(velocidade_rosa, font=("", 20))

    #inputa a velocidade em cada tartaruga a cada loop
    tartaruga_azul.forward(velocidade_azul)
    tartaruga_amarela.forward(velocidade_amarelo)
    tartaruga_laranja.forward(velocidade_laranja)
    tartaruga_rosa.forward(velocidade_rosa)
    Num_loops += 1

#gira o vencedor
def gira_gira(x):
    for i in range(72):
        if x[0]!=0:
            tartaruga_azul.left(5)
            tartaruga_azul.shapesize(5)
        if x[1]!=0:
            tartaruga_amarela.left(5)
            tartaruga_amarela.shapesize(5)
        if x[2]!=0:
            tartaruga_laranja.left(5)
            tartaruga_laranja.shapesize(5)
        if x[3]!=0:
            tartaruga_rosa.left(5)
            tartaruga_rosa.shapesize(5)

#determina o vencedor e o imprime na tela
x = [0 for i in range(4)]        
if tartaruga_amarela.xcor() > tartaruga_azul.xcor() and  tartaruga_amarela.xcor() > tartaruga_rosa.xcor() and tartaruga_amarela.xcor() > tartaruga_laranja.xcor():
    tartaruga_titulo.write("Amarela é Vencedora", font=("", 20, 'italic'))
    x[1] = 1
elif tartaruga_azul.xcor() > tartaruga_amarela.xcor() and  tartaruga_azul.xcor() > tartaruga_rosa.xcor() and tartaruga_azul.xcor() > tartaruga_laranja.xcor():
    tartaruga_titulo.write("Azul é Vencedora", font=("", 20, 'italic'))
    x[0] = 1
elif tartaruga_rosa.xcor() > tartaruga_amarela.xcor() and  tartaruga_rosa.xcor() > tartaruga_azul.xcor() and tartaruga_rosa.xcor() > tartaruga_laranja.xcor():
    tartaruga_titulo.write("Rosa é Vencedora", font=("", 20, 'italic'))
    x[3] = 1
elif tartaruga_laranja.xcor() > tartaruga_amarela.xcor() and  tartaruga_laranja.xcor() > tartaruga_azul.xcor() and tartaruga_laranja.xcor() > tartaruga_rosa.xcor():
    tartaruga_titulo.write("Laranja é Vencedora", font=("", 20, 'italic'))
    x[2] = 1
elif tartaruga_laranja.xcor() == tartaruga_amarela.xcor() == tartaruga_azul.xcor() == tartaruga_rosa.xcor():
    tartaruga_titulo.write("Empate entre todas", font=("", 20, 'italic'))
    x = [1 for i in range(4)]  
elif tartaruga_laranja.xcor() == tartaruga_amarela.xcor() == tartaruga_azul.xcor() and tartaruga_amarela.xcor() > tartaruga_rosa.xcor():
    tartaruga_titulo.write("Empate entre a Laranja e Amarela", font=("", 20, 'italic'))
    x[0] = 1
    x[1] = 1
elif tartaruga_laranja.xcor() == tartaruga_rosa.xcor() == tartaruga_azul.xcor() and tartaruga_azul.xcor() > tartaruga_amarela.xcor():
    tartaruga_titulo.write("Empate entre a Azul, Laranja e Rosa", font=("", 20, 'italic'))
    x[0] = 1 
    x[1] = 1 
    x[2] = 1
elif tartaruga_rosa.xcor() == tartaruga_amarela.xcor() == tartaruga_azul.xcor() and tartaruga_amarela.xcor() > tartaruga_laranja.xcor():
    tartaruga_titulo.write("Empate entre a Azul, Amarela e Rosa", font=("", 20, 'italic'))
    x[0] = 1
    x[3] = 1
    x[1] = 1
elif tartaruga_laranja.xcor() == tartaruga_amarela.xcor() == tartaruga_rosa.xcor() and tartaruga_amarela.xcor() > tartaruga_azul.xcor():
    tartaruga_titulo.write("Empate entre a Amarela, Laranja e Rosa", font=("", 20, 'italic'))
    x[1] = 1
    x[2] = 1
    x[3] = 1
elif tartaruga_azul.xcor() == tartaruga_amarela.xcor() and tartaruga_amarela.xcor() > tartaruga_rosa.xcor() and tartaruga_azul.xcor() > tartaruga_laranja.xcor():
    tartaruga_titulo.write("Empate a Azul e Amarela", font=("", 20, 'italic'))
    x[0] = 1
    x[1] = 1
elif tartaruga_azul.xcor() == tartaruga_rosa.xcor() and tartaruga_azul.xcor() > tartaruga_amarela.xcor()and tartaruga_azul.xcor() > tartaruga_laranja.xcor():
    tartaruga_titulo.write("Empate entre a Azul e Rosa", font=("", 20, 'italic'))
    x[0] = 1
    x[3] = 1    
elif tartaruga_azul.xcor() == tartaruga_laranja.xcor() and tartaruga_azul.xcor() > tartaruga_amarela.xcor() and tartaruga_azul.xcor() > tartaruga_rosa.xcor():
    tartaruga_titulo.write("Empate entre a Azul e Laranja", font=("", 20, 'italic'))
    x[0] = 1
    x[2] = 1
elif tartaruga_rosa.xcor() == tartaruga_amarela.xcor() and tartaruga_amarela.xcor() >tartaruga_azul.xcor() and tartaruga_amarela.xcor() > tartaruga_laranja.xcor():
    tartaruga_titulo.write("Empate entre a Amerela e Rosa", font=("", 20, 'italic'))
    x[3] = 1
    x[1] = 1
elif tartaruga_laranja.xcor() == tartaruga_amarela.xcor() and tartaruga_amarela.xcor() > tartaruga_azul.xcor() and tartaruga_amarela.xcor() > tartaruga_rosa.xcor():
    tartaruga_titulo.write("Empate entre a Amarela e Laranja", font=("", 20, 'italic'))
    x[2] = 1
    x[1] = 1
else:
    tartaruga_titulo.write("Empate entre a Laranja e Rosa", font=("", 20, 'italic'))   
    x[3] = 1
    x[2] = 1   
gira_gira(x)       
    

window.mainloop()
