from EscuderiaMoralmenteCorrecta import Escuderia

escuderias=[]

numeroEscuderia=0

while(numeroEscuderia<2):
    escuderia = Escuderia()
    escuderia.nombre=input("Digite el nombre de la escuderia: ")
    escuderia.motor=input("Digite el motor de la escuderia: ")
    escuderia.piloto1=input("Digita el nombre del primer piloto: ")
    escuderia.piloto2=input("Digita el nombre del segundo piloto: ")
    escuderia.costoAnual=int(input("Digite el costo anual: "))
    
    escuderias.append(escuderia)
    numeroEscuderia+=1
    
if(escuderias[0].costoAnual == escuderias[1].costoAnual):
    print("Las escuderias tienen el mismo valor")
elif(escuderias[0].costoAnual > escuderias[1].costoAnual):
    print(f"La escuderia mas cara es:  {escuderias[0].nombre}")
else:
    print(f"La escuderia mas cara es:  {escuderias[1].nombre}")
    
#Por que se llama The wekeend
# Comenzó a consumir drogas a los 11 años, de fumar marihuana a consumo de 
# Ketamina o MDMA, algún robo en supermercado y dejó de estudiar “un fin de semana” con un amigo. 
# Y de esa deserción viene su nombre artístico, que fue modificado para no entrar en conflicto con la 
# banda canadiense The weekend.