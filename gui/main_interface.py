from tkinter import *
import tkinter as tk
import time
from expanded_basket import ExpandedBasket
from random import randint

'''
[TODO]
*Implement timer
*Fill framePlaceholder
[NOTES]
Must include the resource file 'arrows.gif' and expanded_basket.py in the same directory to run correctly
'''



class MainInterface:
    
    def __init__(self, root):
        '''Basic window setup'''
        self.root = root
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.wm_title("Python ALL Project")
        self.root.config(background = "#FFFFFF")
        self.root.geometry("1025x800")
        self.time_str = StringVar()

        
        


        def frames(self):
            '''Create and place frames'''
            self.frameMenu = Frame(self.root, width=225, height = 600, background="royalblue")
            self.frameMenu.grid(row=0, column=1, padx=0, pady=0, sticky="nes")

            self.frameBasket = Frame(self.root, width=200, height = 300, background="white")
            self.frameBasket.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.795)

            self.framePlaceholder = Frame(self.root, width=200, height = 200, background="white")
            self.framePlaceholder.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.46)

            self.frameGame = Frame(self.root, width=900, height = 800, background="white")
            self.frameGame.grid(row=0, column=0, padx=0, pady=0, sticky="wnes" )

            self.frameTimer = Frame(self.root, width=200, height = 100, background="white")
            self.frameTimer.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.25)

            self.lineframe1 = Frame(self.root, width=200, height = 1, background="lightgrey")
            self.lineframe1.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.65)

            self.lineframe2 = Frame(self.root, width=200, height = 1, background="lightgrey")
            self.lineframe2.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.371)

            self.lineframe3 = Frame(self.root, width=200, height = 1, background="lightgrey")
            self.lineframe3.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.222)
      

        def buttons(self):
            '''Create and place buttons'''
            self.distributeButton = Button(self.frameMenu, text="Distribute items", command = lambda: distributeItems(), background="royalblue", fg="white")
            self.distributeButton.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.100)

            self.image = tk.PhotoImage(file="arrows.gif")
            self.expandButton = Button(self.frameBasket, image=self.image, background="white", command = lambda: expandedBasket())
            self.expandButton.place(anchor="c", relx=0.9, rely=0.06)
            
            #Creates the related timer buttons & adds them to 'frameTimer',_Button1-3 is the duration selected in seconds
            self._button1 = Button(self.frameTimer, text='1 minute', command= lambda a=60: timerHandler(a))
            self._button2 = Button(self.frameTimer, text='2 minutes', command= lambda b=120: timerHandler(b))
            self._button3 = Button(self.frameTimer, text='4 minutes', command= lambda c=240: timerHandler(c))
            
            self._button1.place(anchor="c", relx=0.15, rely=0.87)
            self._button2.place(anchor="c", relx=0.50, rely=0.87)
            self._button3.place(anchor="c", relx=0.85, rely=0.87)
             

        def labels(self):
            '''Create and place labels'''
            basketLabel = Label(self.frameBasket, text="Basket", background="white", fg="mediumblue")
            basketLabel.place(anchor="c", relx=0.5, rely=0.06)

            phLabel = Label(self.framePlaceholder, text="PLACEHOLDER", background="white", fg="mediumblue")
            phLabel.place(anchor="c", relx=0.5, rely=0.08)

            timerLabel = Label(self.frameTimer, text="Timer", background="white", fg="mediumblue")
            timerLabel.place(anchor="c", relx=0.5, rely=0.14)

            self.timerActiveLabel = Label(self.frameTimer, text="UPDATE", background="white", fg="mediumblue")
            self.timerActiveLabel.place(anchor="c", relx=0.5, rely=0.40)


        def map(self):
            self.canvas = Canvas(self.frameGame,width = 800, height = 800, bg = 'black')
            self.canvas.pack(expand = YES, fill = BOTH)
            self.map = PhotoImage(file = 'map.png')
            self.canvas.create_image(0, 0, image = self.map, anchor = NW)




            '''Below sets out the item locations areas and the walls to the maze'''
        ###ITEM HOLDER BOXES
            itemHolder = self.canvas.create_rectangle(735, 0, 768, 161, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(639, 32, 736, 65, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(575, 192, 673, 257, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(575, 352, 705, 417, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(575, 352, 705, 417, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(575, 480, 705, 545, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(639, 640, 705, 737, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(511, 640, 577, 737, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(95, 96, 193, 193, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(95, 256, 193, 353, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(95, 416, 193, 513, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(127, 640, 225, 737, fill='', width=0)


            #EXTERIOR WALLS
            walls = self.canvas.create_rectangle(0, 0, 33, 801, fill='', width=0)
            walls = self.canvas.create_rectangle(0, 0, 801, 33, fill='', width=0)
            walls = self.canvas.create_rectangle(0, 768, 353, 801, fill='', width=0)
            walls = self.canvas.create_rectangle(416, 768, 801, 801, fill='', width=0)
            walls = self.canvas.create_rectangle(767, 0, 801, 801, fill='', width=0)

            #INTERIOR WALLS
            walls = self.canvas.create_rectangle(32, 576, 353, 609, fill='', width=0)
            walls = self.canvas.create_rectangle(415, 576, 768, 609, fill='', width=0)
            walls = self.canvas.create_rectangle(416, 704, 449, 769, fill='', width=0)
            walls = self.canvas.create_rectangle(320, 704, 353, 769, fill='', width=0)
            walls = self.canvas.create_rectangle(415, 608, 449, 641, fill='', width=0)
            walls = self.canvas.create_rectangle(319, 608, 353, 641, fill='', width=0)
            walls = self.canvas.create_rectangle(512, 288, 768, 321, fill='', width=0)
            walls = self.canvas.create_rectangle(479, 32, 513, 129, fill='', width=0)
            walls = self.canvas.create_rectangle(479, 192, 513, 417, fill='', width=0)
            walls = self.canvas.create_rectangle(479, 480, 513, 577, fill='', width=0)
            walls = self.canvas.create_rectangle(255, 96, 289, 577, fill='', width=0)



            #Create user controlled robot
            player=self.canvas.create_rectangle(364,727,404,767,fill = 'green',width=2)

            #Robot Location Setter
            x1,y1,x2,y2=self.canvas.coords(player)
            
            '''Below code is used for controlling the robot, temporary code that will be wiped when pathfinding algorithm has been implemented'''
            #Move robot left
            def leftKey(event):
                x1,y1,x2,y2=self.canvas.coords(player)
                self.canvas.coords(player,x1-5,y1,x2-5,y2)
                currentLocation = self.canvas.coords(player)
                objectsTouching = (self.canvas.find_overlapping(currentLocation[0],currentLocation[1],currentLocation[2],currentLocation[3]))
                if 2<= (objectsTouching[-2]) <= 13:
                    print('You have hit the items!!!')
                if 14<= (objectsTouching[-2]) <= 29:
                    print('You have hit the wall!!!')

            #Move robot right
            def rightKey(event):
                x1,y1,x2,y2=self.canvas.coords(player)
                self.canvas.coords(player,x1+5,y1,x2+5,y2)
                currentLocation = self.canvas.coords(player)
                objectsTouching = (self.canvas.find_overlapping(currentLocation[0],currentLocation[1],currentLocation[2],currentLocation[3]))
                if 2<= (objectsTouching[-2]) <= 13:
                    print('You have hit the items!!!')
                if 14<= (objectsTouching[-2]) <= 29:
                    print('You have hit the wall!!!')

            #Move robot up
            def upKey(event):
                x1,y1,x2,y2=self.canvas.coords(player)
                self.canvas.coords(player,x1,y1-5,x2,y2-5)
                currentLocation = self.canvas.coords(player)
                objectsTouching = (self.canvas.find_overlapping(currentLocation[0],currentLocation[1],currentLocation[2],currentLocation[3]))
                if 2<= (objectsTouching[-2]) <= 13:
                    print('You have hit the items!!!')
                if 14<= (objectsTouching[-2]) <= 29:
                    print('You have hit the wall!!!')


            #Move robot down
            def downKey(event):
                x1,y1,x2,y2=self.canvas.coords(player)
                self.canvas.coords(player,x1,y1+5,x2,y2+5)
                currentLocation = self.canvas.coords(player)
                objectsTouching = (self.canvas.find_overlapping(currentLocation[0],currentLocation[1],currentLocation[2],currentLocation[3]))
                if 2<= (objectsTouching[-2]) <= 13:
                    print('You have hit the items!!!')
                if 14<= (objectsTouching[-2]) <= 29:
                    print('You have hit the wall!!!')


            #move robot using keys
            self.canvas.bind('<Left>', leftKey)
            self.canvas.bind('<Right>', rightKey)
            self.canvas.bind('<Up>', upKey)
            self.canvas.bind('<Down>', downKey)
            self.canvas.focus_set()








        def timerHandler(duration):
            self.duration = duration
            
                
        def distributeItems():
            '''TODO: Randomly places items within map & start timer'''
            sys.stdout.write("Distribute pressed \n")

            self.item = PhotoImage(file = 'item.png')
            tup = ((105,105),(105,130),(105, 155),(105, 180),(130, 105),(155, 105),(180, 105),(180, 130),(180, 155)
                   ,(180, 180),(155, 180),(130, 180),(105, 265),(105, 290),(105, 315),(105, 340),(130, 340)
                   ,(155, 340),(180, 340),(180, 290),(180, 265),(180, 315),(155, 265),(130, 265),(105, 425)
                   ,(105, 450),(105, 475),(105, 500),(130, 425),(155, 425),(180, 425),(180, 450),(180, 475)
                   ,(180, 500),(155, 500),(130, 500),(135, 650),(135, 675),(135, 700),(135, 725),(160, 650)
                   ,(185, 650),(210, 650),(210, 675),(210, 700),(210, 725),(185, 725),(160, 725),(650, 50)
                   ,(675, 50),(700, 50),(725, 50),(750, 75),(750, 100),(750, 125),(750, 150),(586, 200)
                   ,(611, 200),(636, 200),(661, 200),(586, 246),(611, 246),(636, 246),(661, 246),(586, 360)
                   ,(611, 360),(636,360),(661,360),(686,360),(586, 406),(611, 406),(636, 406),(661, 406)
                   ,(686, 406),(586, 490),(611, 490),(636, 490),(661, 490),(686, 490),(586, 536),(611, 536)
                   ,(636, 536),(661, 536),(686, 536),(520, 650),(520, 675),(520, 700),(520, 725),(565, 650)
                   ,(565, 675),(565, 700),(565, 725),(650, 650),(650, 675),(650, 700),(650, 725),(695, 650)
                   ,(695, 675),(695, 700),(695, 725))

            for x in range (20):
                rnd = randint(0,99)
                self.canvas.create_image(tup[rnd], image = self.item)
            

        def expandedBasket():
            '''Launches expanded basket'''
            sys.stdout.write("Expand pressed \n")
            self.frameMenu.destroy()
            self.frameGame.destroy()
            EB = ExpandedBasket(root)
            
        frames(self)
        buttons(self)
        labels(self)
        map(self)

        def collisionDetection():
            '''Collision detection'''


def main():
    root = Tk()
    mainInterface = MainInterface(root)
    root.mainloop()

if __name__ == '__main__':
    sys.exit(main())
