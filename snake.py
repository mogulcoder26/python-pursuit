from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:   
    def __init__(self):
        self.segment_number =3
        self.starting_coords =[(0, 0), (-20, 0), (-40, 0)]
        self.segment_array = []
        self.createSnake()
        self.head =self.segment_array[0]

    def createSnake(self):

        for coords in self.starting_coords:
            segment_new = Turtle('square')
            segment_new.penup()
            segment_new.width(0.1)
            segment_new.color('#fff')
            segment_new.goto(coords)
            self.segment_array.append(segment_new)
    
    def move(self):

        for seg_num in range(len(self.segment_array) -1 ,0 ,-1):
            new_x  = self.segment_array[seg_num -1 ].xcor()
            new_y  = self.segment_array[seg_num -1 ].ycor()
            self.segment_array[seg_num].goto(new_x,new_y)

        #Moving the front head up which is being followed by the rest of the body via the upper for loop
        self.head.forward(MOVE_DISTANCE)
        # self.segment_array[0].left(90)

    def up(self):
            if(self.head.heading()==270.0):
                return
            self.head.setheading(90.0)
    def down(self):
        if(self.head.heading()==90.0):
            return
        self.head.setheading(270.0)
    
    def left(self):
            if(self.head.heading()==0.0):
                  return
            self.head.setheading(180.0)
    
    def right(self):
          if(self.head.heading()==180.0):
            return
          self.head.setheading(0.0)
          
    def SnakeAteFoodSoSnakeExtends(self):
         added_segment = Turtle('square')
         added_segment.penup()
         added_segment.color('#fff')
         self.segment_array.append(added_segment)         
