from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.geometry("620x600")                  
root.resizable(False,False)
root.title("Calculator Commission")
root.configure(bg="#C1ECFA")

# ฟังค์ชั่นที่ใช้เรียกผลลัพพ์และคำนวณ
Label(root,text="Calculator Commission From Python",font="arial 25",bg="#3090C7").place(x=40,y=30)

def calculate():
   try: 
      locks = int(lockEntry.get())
      stocks = int(stockEntry.get())
      barrels = int(barrelEntry.get())
      
      lockPrice = 45.0
      stockPrice = 30.0 
      barrelPrice = 25.0
      totalLocks = 0
      totalStocks = 0
      totalBarrels = 0

      if (type(locks) == int and type(stocks) == int and type(barrels) == int ) :
         if(locks < 1 or locks > 70):
            mb.showwarning("Alert","Lock is out of range")
         elif(stocks < 1 or stocks > 80):
            mb.showwarning("Alert","Stock is out of range")
         elif(barrels < 1 or barrels > 90):
            mb.showwarning("Alert","Barrel is out of range")
         else:
            
            totalLocks = totalLocks + locks
            totalStocks = totalStocks + stocks
            totalBarrels = totalBarrels + barrels 
                
            lockSales = lockPrice * totalLocks
            stockSales = stockPrice * totalStocks
            barrelSales = barrelPrice * totalBarrels 
            sale = lockSales + stockSales + barrelSales
                
            if(sale > 1800.0):
               commission = 0.10 * 1000.0
               commission = commission + (800.0 * 0.15)
               commission = commission + (sale - 1800.0) * 0.20
                    
            elif(sale > 1000):
               commission = 0.10 * 1000.0
               commission = commission + (sale - 1000) * 0.15
                    
            else:
               commission = 0.10 * sale
                
                #display
            if (commission.is_integer()):
               result = round(commission)
               text_Output.configure(state = NORMAL)
               text_Output.insert("1.0","-------------------------------------------------------- \n")
               text_Output.insert("2.0","Lock = %d \nStock = %d \nBarrel = %d \nSale = %d \nCommission = %d \n"
                                  %(locks,stocks,barrels,sale,result))
               text_Output.configure(state = DISABLED)
               lockEntry.delete(0,END)
               stockEntry.delete(0,END)
               barrelEntry.delete(0,END)

               
               
            else:
               text_Output.configure(state = NORMAL)
               result = str(commission)
               text_Output.insert("1.0","-------------------------------------------------------- \n")
               text_Output.insert("2.0","Lock = %d \nStock = %d \nBarrel = %d \nSale = %d \nCommission = %s \n"
                                  %(locks,stocks,barrels,sale,result))
               text_Output.configure(state = DISABLED)
               lockEntry.delete(0,END)
               stockEntry.delete(0,END)
               barrelEntry.delete(0,END)
        
   except ValueError :
        
         locks=(lockEntry.get())
         stocks=(stockEntry.get())
         barrels=(barrelEntry.get())

         
         if (locks == "" or stocks == "" or barrels == ""):   
            mb.showwarning("Alert","ไม่พบค่าในการคำนวณ !!!")
            
            
         else :
            mb.showwarning("Alert","กรุณาใส่แต่ตัวเลขเท่านั้น..")

def clear():
    lockEntry.delete(0,END)
    stockEntry.delete(0,END)
    barrelEntry.delete(0,END)
    text_Output.delete(0,END)

Label(text="Locks",font="arial 14",bg="#C1ECFA").place(x=90,y=110)
Label(text="Stocks",font="arial 14",bg="#C1ECFA").place(x=90,y=160)
Label(text="Barrels",font="arial 14",bg="#C1ECFA").place(x=90,y=210)

lockValue = StringVar()
stockValue = StringVar()
barrelValue = StringVar()

lockEntry=Entry(root,textvariable=lockValue,width=30,bd=3,font=20)
lockEntry.place(x=180,y= 110)

stockEntry=Entry(root,textvariable=stockValue,width=30,bd=3,font=20)
stockEntry.place(x=180,y= 160)

barrelEntry=Entry(root,textvariable=barrelValue,width=30,bd=3,font=20)
barrelEntry.place(x=180,y= 210)

text_Output = Text(root ,font=("arial " , 18),width=35,height=9,bg="#3090C7")
text_Output.configure(state = DISABLED)
text_Output.place(x=80,y=347)

bt = Button(text="Calculate",font="arial 14",bg="green",fg="White",width=11,height=2,command=calculate).place(x=120,y=260)
dt = Button(text="Delete",font="arial 14",bg="red",fg="White",width=11,height=2,command=clear).place(x=370,y=260)

root.mainloop()