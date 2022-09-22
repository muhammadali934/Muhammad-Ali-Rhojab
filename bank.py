#bank.py


salam = input("Greeting :").lower().strip()

if salam == ("hello") :
    print("$0")
elif salam.startswith ("h") :
    print("$20")
else :
    print("$100")