# 작성자: 송영준
# 작성일: 2026-10-03
# 문제: 터틀 그래픽에서 각각의 거북이는 객체이다. 2개의 거북이를 생성하여 
#       다음과 같이 서로 다른 방향으로 움직이도록 하자.

import turtle
t = turtle.Turtle()
t.shape("turtle")

lee = turtle.Turtle()
lee.shape("circle")

t.forward(100)
t.right(90)
t.forward(20)
t.left(90)
t.forward(100)

lee.left(180)
lee.forward(100)
lee.right(90)
lee.forward(20)
lee.left(90)
lee.forward(100)

turtle.done()
