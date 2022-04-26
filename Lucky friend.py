from tkinter import *
import random
root.tk()

root.geometry("400x400")
root.title("Luck Friend Wheel")

list1 = ["Ashaaz", "Atharva", "Aadwik", "Arv", "Sagar"]
print(list1)

def random_number():
    random_no = random.randint(0,4)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("your lucky friend is :" + random_lucky_friend)
    
    btn1 = Button(root)
    btn1 = Button(root, text="Who is your Lucky Friend?", command = random_number)
    btn1.place(relx= 0.5, rely = 0.5, anchor = CENTER)
    
    root.mainloop()