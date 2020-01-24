import sys


if len(sys.argv) >= 1:
    with open(sys.argv[1],"rb") as archivo:
        with open("sav.dat","wb") as sav:
            guardar = archivo.read(32784)
            sav.write(guardar)

        print("[+] Done! save.dat created")
else:
    print("error method of use Sav2VC.py file.dat")


