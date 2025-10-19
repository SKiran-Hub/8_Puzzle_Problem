import tkinter as tk
from tkinter import simpledialog, messagebox
import random, heapq, copy, time

GOAL = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# ---------- Core Utilities ----------
def find_blank(p):
    for i in range(3):
        for j in range(3):
            if p[i][j]==0:
                return i,j

def flatten(p): return [n for row in p for n in row]

def is_solvable(flat):
    inv=0
    for i in range(8):
        for j in range(i+1,9):
            if flat[i] and flat[j] and flat[i]>flat[j]:
                inv+=1
    return inv%2==0

def heuristic(p):
    d=0
    for i in range(3):
        for j in range(3):
            v=p[i][j]
            if v!=0:
                gx,gy=divmod(v-1,3)
                d+=abs(gx-i)+abs(gy-j)
    return d

def neighbors(p):
    i,j=find_blank(p)
    moves=[]
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        x,y=i+dx,j+dy
        if 0<=x<3 and 0<=y<3:
            np=copy.deepcopy(p)
            np[i][j],np[x][y]=np[x][y],np[i][j]
            moves.append(np)
    return moves

def a_star(start):
    frontier=[]
    heapq.heappush(frontier,(heuristic(start),start))
    came_from={}
    g={str(start):0}
    while frontier:
        _,cur=heapq.heappop(frontier)
        if cur==GOAL:
            path=[cur]
            while str(cur) in came_from:
                cur=came_from[str(cur)]
                path.append(cur)
            return path[::-1]
        for nxt in neighbors(cur):
            ng=g[str(cur)]+1
            if str(nxt) not in g or ng<g[str(nxt)]:
                g[str(nxt)]=ng
                heapq.heappush(frontier,(ng+heuristic(nxt),nxt))
                came_from[str(nxt)]=cur
    return None

# ---------- GUI ----------
class PuzzleGUI:
    TILE_SIZE=100
    COLORS={0:"#282c34",1:"#e5c07b",2:"#56b6c2",3:"#c678dd",
            4:"#61afef",5:"#98c379",6:"#d19a66",7:"#be5046",8:"#56b6c2"}

    def __init__(self,root):
        self.root=root
        self.root.title("8 Puzzle – Interactive GUI")
        self.root.config(bg="#21252b")

        self.canvas=tk.Canvas(root,width=3*self.TILE_SIZE,
                              height=3*self.TILE_SIZE,bg="#21252b",highlightthickness=0)
        self.canvas.pack(padx=20,pady=10)
        self.canvas.bind("<Button-1>",self.click_tile)

        controls=tk.Frame(root,bg="#21252b")
        controls.pack()
        tk.Button(controls,text="Shuffle",command=self.shuffle,
                  bg="#61afef",fg="white",font=("Helvetica",12,"bold")).grid(row=0,column=0,padx=5)
        tk.Button(controls,text="Solve (A*)",command=self.solve,
                  bg="#98c379",fg="white",font=("Helvetica",12,"bold")).grid(row=0,column=1,padx=5)
        tk.Button(controls,text="Custom Start",command=self.custom_start,
                  bg="#c678dd",fg="white",font=("Helvetica",12,"bold")).grid(row=0,column=2,padx=5)
        tk.Button(controls,text="Reset",command=self.reset,
                  bg="#e06c75",fg="white",font=("Helvetica",12,"bold")).grid(row=0,column=3,padx=5)

        self.status=tk.Label(root,text="Moves: 0",fg="white",bg="#21252b",font=("Helvetica",14))
        self.status.pack(pady=5)

        self.puzzle=copy.deepcopy(GOAL)
        self.moves=0
        self.draw()

    # --- Drawing and Updates ---
    def draw(self):
        self.canvas.delete("all")
        for i in range(3):
            for j in range(3):
                val=self.puzzle[i][j]
                x1,y1=j*self.TILE_SIZE,i*self.TILE_SIZE
                x2,y2=x1+self.TILE_SIZE,y1+self.TILE_SIZE
                color=self.COLORS[val]
                if val!=0:
                    self.canvas.create_rectangle(x1,y1,x2,y2,fill=color,outline="#21252b",width=3)
                    self.canvas.create_text((x1+x2)//2,(y1+y2)//2,text=str(val),
                                            fill="white",font=("Helvetica",32,"bold"))
                else:
                    self.canvas.create_rectangle(x1,y1,x2,y2,fill="#21252b",outline="#3e4451",width=2)
        self.status.config(text=f"Moves: {self.moves}")

    def click_tile(self,event):
        j=event.x//self.TILE_SIZE
        i=event.y//self.TILE_SIZE
        bi,bj=find_blank(self.puzzle)
        if abs(bi-i)+abs(bj-j)==1:
            self.puzzle[bi][bj],self.puzzle[i][j]=self.puzzle[i][j],self.puzzle[bi][bj]
            self.moves+=1
            self.draw()
            if self.puzzle==GOAL:
                messagebox.showinfo("🎉 Congratulations!",f"You solved the puzzle in {self.moves} moves!")

    # --- Controls ---
    def shuffle(self):
        flat=list(range(9))
        while True:
            random.shuffle(flat)
            if is_solvable(flat): break
        self.puzzle=[flat[0:3],flat[3:6],flat[6:9]]
        self.moves=0
        self.draw()

    def reset(self):
        self.puzzle=copy.deepcopy(GOAL)
        self.moves=0
        self.draw()

    def custom_start(self):
        s=simpledialog.askstring("Custom Start",
            "Enter 9 numbers (0–8) separated by spaces (0 = blank):\nExample: 1 2 3 4 0 5 6 7 8")
        if not s: return
        try:
            nums=[int(x) for x in s.split()]
            if sorted(nums)!=list(range(9)):
                raise ValueError
            if not is_solvable(nums):
                messagebox.showerror("Invalid","That configuration is not solvable.")
                return
            self.puzzle=[nums[0:3],nums[3:6],nums[6:9]]
            self.moves=0
            self.draw()
        except:
            messagebox.showerror("Error","Please enter valid 0–8 numbers separated by spaces.")

    def solve(self):
        path=a_star(self.puzzle)
        if not path:
            messagebox.showerror("Error","No solution found!")
            return
        self.animate(path)

    def animate(self,path):
        for state in path:
            self.puzzle=state
            self.draw()
            self.root.update()
            time.sleep(0.35)
        messagebox.showinfo("🤖 AI Solved!",f"AI solved the puzzle in {len(path)-1} moves!")

# ---------- Run ----------
if __name__=="__main__":
    root=tk.Tk()
    app=PuzzleGUI(root)
    root.mainloop()
