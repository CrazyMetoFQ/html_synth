from flask import Flask, render_template, request
import random
import itertools


text_colors = [(random.randint(1,256),random.randint(1,256),random.randint(1,256)) for i in range(50)]
bg_colors = [(random.randint(1,256),random.randint(1,256),random.randint(1,256)) for i in range(50)]
font_sizes = range(15,41,5)
font_weights =  range(100,1001, 100)
font_familys =  ["serif","sans-serif","cursive","fantasy","monospace"]
font_styles  =  ["normal","italic"]
font_variants=  ["normal","small-caps"]
text_align = ["left","center","right"]
rotations = [-45,-30,-30,-20,-10,0,0,0,0,0,10,20,30,30,45]

all_things = (text_colors ,bg_colors,font_familys,font_styles, font_sizes,font_weights,font_variants,text_align, rotations)

totn = 15
all_l = [[random.choice(i) for i in all_things] for _ in range(totn)]

# def rnd_l():
#   for _ in range(totn):
#     yield [random.choice(i) for i in all_stuff]

# all_l = rnd_l() 


class items_stuff:
    
  alphabets_U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  alphabets_L = alphabets_U.lower()

  nums = "12345567890"

  all_stuff = alphabets_L+alphabets_U+nums
  # all_stuff = "ab"




  def __init__(self) -> None:
    self.iposat = -1
    self.sposat = -1
    self.tposat = -1
    self.cylce_num = 0
    self.is_over = False



  def getitem(self):
    
    if self.is_over:
      print("over")
      return False
    else:
      pass

    self.tposat += 1
    print("tposat",self.tposat)
    
    if self.tposat%totn == 0:
      print("ipos check",1)  

      if self.iposat < len(items_stuff.all_stuff)-1:
        self.iposat += 1
        print("ipos icrement",2)

      else:
        print("ipos greater",3)
        self.is_over = True
        return False
    
    if self.sposat < totn-1 :
        print("spos increment",4)
        self.sposat += 1
    else:
        print("spos reset",5)
        self.sposat = 0
    
    print(self.iposat,self.sposat)
    return (items_stuff.all_stuff[self.iposat],self.sposat,all_l[self.sposat])




itg = items_stuff()







app = Flask(__name__)

sym_text = "Click_me"
sl = all_l[0]
cstate = True
imno = "start"


@app.route("/", methods=["GET", "POST"])
def index():
  
  global sym_text
  global sl
  global cstate
  global imno
  
  if request.method == "POST":
    
    item = itg.getitem()
    print(item)

    if item == False:
      print("doing it")
      cstate = False
    else:
      sym_text,imno,sl = item

  print(cstate)
  if cstate == True:
    print("nigga")
    return render_template("index.html",
                          sym_text=sym_text,
                          save_name=f"img_{sym_text}_{imno}.png",
                          text_color= f"rgb{sl[0]}",
                          bg_color= f"rgb{sl[1]}",
                          font_family =  sl[2] ,
                          font_style  =  sl[3],
                          font_size   =  f"{sl[4]}px" ,
                          font_weight =  sl[5],
                          font_variant=  sl[6],
                          text_align = sl[7],
                          rotation = sl[8]
                          )
  else:

    print("wtf")
    return render_template("over.html")

if __name__ == "__main__":
  app.run(debug=True)
