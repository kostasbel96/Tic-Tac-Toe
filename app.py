import tkinter as tk

class MyApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(0,0)
        self.root.geometry("400x400+500+200")
        self.lines = []
        self.x = []
        self.o = []
        self.ovals = []
        self.playerOne = True
        self.game = {5:'', 6:'', 7:'', 8:'', 9:'', 10:'', 11:'', 12:'', 13:''}
        self.winner_cord = ((5,6,7), (8,9,10), (11,12,13), (5,8,11), (6,9,12), (7,10,13), (5,9,13), (11,9,7))
        self.coord_o = []
        self.coord_x = []
        self.finish_game = False
        self.createBoard()

    def createBoard(self):
        self.canvas = tk.Canvas(self.root,width=400,height=400,bg='red')
        self.canvas.pack()
        self.lines.append(self.canvas.create_line(60,150,340,150,fill='black',width=5))  
        self.lines.append(self.canvas.create_line(60,250,340,250,fill='black',width=5))  
        self.lines.append(self.canvas.create_line(150,60,150,340,fill='black',width=5))
        self.lines.append(self.canvas.create_line(250,60,250,340,fill='black',width=5))
        
        self.ovals.append(self.canvas.create_oval(70,70,140,140,width=0,fill='red'))
        self.ovals.append(self.canvas.create_oval(70,160,140,240,width=0,fill='red'))
        self.ovals.append(self.canvas.create_oval(70,260,140,340,width=0,fill='red'))

        self.ovals.append(self.canvas.create_oval(160,70,240,140,width=0,fill='red'))
        self.ovals.append(self.canvas.create_oval(160,160,240,240,width=0,fill='red'))
        self.ovals.append(self.canvas.create_oval(160,260,240,340,width=0,fill='red'))

        self.ovals.append(self.canvas.create_oval(260,70,340,140,width=0,fill='red'))
        self.ovals.append(self.canvas.create_oval(260,160,340,240,width=0,fill='red'))
        self.ovals.append(self.canvas.create_oval(260,260,340,340,width=0,fill='red'))

        self.canvas.img2 = tk.PhotoImage(file='o.gif')
        self.canvas.img = tk.PhotoImage(file='x.gif')
        self.canvas.bind("<Button-1>",self.click)

        self.turnLabel = tk.Label(self.canvas,text="player one(x)",bg="red")
        self.canvas.create_window(50,50,window=self.turnLabel)

        self.reset = tk.Button(self.canvas, text='reset', command=self.reset)
        self.canvas.create_window(20,15,window=self.reset)

    def click(self, event):
        finish = self.check_winner()
        print(finish)
        if len(self.canvas.find_overlapping(event.x,event.y,event.x,event.y)) > 0 and self.playerOne and not finish:
            
            self.canvas.create_window(50,50,window=self.turnLabel)
            for line in self.lines:
                if line in self.canvas.find_overlapping(event.x,event.y,event.x,event.y):
                    return
            for x in self.x:
                if x in self.canvas.find_overlapping(event.x,event.y,event.x,event.y):
                    return
            for o in self.o:
                if o in self.canvas.find_overlapping(event.x,event.y,event.x,event.y):
                    return    
            for oval in self.ovals:
                if oval in self.canvas.find_overlapping(event.x,event.y,event.x,event.y):                
                    self.draw_x(self.canvas.coords(oval)[0]+35,self.canvas.coords(oval)[1]+35)
                    self.playerOne = False
                    self.game[oval] = 'x'       
        elif len(self.canvas.find_overlapping(event.x,event.y,event.x,event.y)) > 0 and not self.playerOne and not finish:
            self.turnLabel.config(text="player two(o)")
            for line in self.lines:
                if line in self.canvas.find_overlapping(event.x,event.y,event.x,event.y):
                    return
            for x in self.x:
                if x in self.canvas.find_overlapping(event.x,event.y,event.x,event.y):
                    return
            for o in self.o:
                if o in self.canvas.find_overlapping(event.x,event.y,event.x,event.y):
                    return    
            for oval in self.ovals:
                if oval in self.canvas.find_overlapping(event.x,event.y,event.x,event.y):                
                    self.draw_o(self.canvas.coords(oval)[0]+35,self.canvas.coords(oval)[1]+35)
                    self.playerOne = True
                    self.game[oval] = 'o'

        self.check_winner()            
        

    def reset(self):
        for x in self.x:
            self.canvas.delete(x)
        for o in self.o:
            self.canvas.delete(o)
        self.x = []
        self.o = []
        for key in self.game:
            self.game[key] = ''
        self.coord_o = [] 
        self.coord_x = []  
        self.canvas.delete(self.text)
        self.finish_game = False

    def check_winner(self):
        
        for key in self.game:
            if self.game[key] == 'o' and key not in self.coord_o:
                self.coord_o.append(key)
            elif self.game[key] == 'x' and key not in self.coord_x:
                self.coord_x.append(key)
        for c in self.winner_cord:
            if set(c).issubset(self.coord_o) and not self.finish_game:
                self.text = self.canvas.create_text(200,30,text="Player 2(o) wins")
                self.finish_game = True
                return True
            elif set(c).issubset(self.coord_x) and not self.finish_game:
                self.text = self.canvas.create_text(200,30,text="Player 1(x) wins")
                self.finish_game = True
                return True
        if self.finish_game:
            return True
        else:return False               

    def draw_x(self,x,y):
        if self.turnLabel['text'].lower() == 'player one(x)':
            self.x.append(self.canvas.create_image(x,y,image=self.canvas.img))
            self.turnLabel.config(text="player two(o)")

    def draw_o(self,x,y):
        if self.turnLabel['text'].lower() == 'player two(o)':
            self.o.append(self.canvas.create_image(x,y,image=self.canvas.img2))    
            self.turnLabel.config(text="player one(x)")

if __name__ == '__main__':
    root = tk.Tk()
    MyApp(root)
    root.mainloop()