from operator import truediv
import random 
input ("Adad Az 1 Ta 100 Dar Nazar Begirid Va Enter Bezanid. : ")
zoj = True if input("Adad Shoma Zoj Ast? (y/n) ") == "y" else False

x = 0
start = 0 if zoj else 1
end = 100 if zoj else 100

while(x == 0):
    hads = random.randrange(start , end , 2)
    print(hads)
    Result = input("Aya Adad Dorost Ast (d/n) : ")
    if Result == "n":
        adad = input( "Agar Adad Mored Nazar Kuchek Tar Ast (k) Ra Vared Konid Va Agar Bozorg Tar Ast (b) Ra Vared Konid : ")
        if adad == "k":
            end = hads
            continue
        elif adad == "b":
            start = hads
            continue
    else:
        break

print("I Found Your Number... ")
