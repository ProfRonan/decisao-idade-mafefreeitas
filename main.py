i= int(input("digite sua idade:"))
eita=True
if i<0:
    eita=False
    print("impossível")
if i< 18:
     eita=False
     print("não precisa se alistar")
if i>18 and i<65:
    eita=False
    print("nao esqueça de votar na proxima eleição.")
if i>65:
    eita=False
    print("vá descansar")
if eita:
    print("eita!")
