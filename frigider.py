from electrocasnice_mari import Electrocasnice_mari


class Frigider(Electrocasnice_mari):

    def __init__(self,capacitate_congelator,capacitate_frigider,adancime,inaltime,latime,pret,consum,producator,cod_produs):
        self.capacitate_congelator=capacitate_congelator
        self.capacitate_frigider=capacitate_frigider
        super().__init__(adancime,inaltime,latime,pret,consum,producator,cod_produs)

    def __str__(self):
        return str(self.adancime) + " " + str(self.inaltime) + " " + str(self.latime) + " " + str(self.pret) \
               + " " + str(self.consum) + " " + str(self.producator) + " " + str(self.cod_produs)\
               +" "+str(self.capacitate_congelator)+" "+str(self.capacitate_frigider)


print("################# INSTANTE CLASA FRIGIDER ################\n")

f=Frigider(150,100,100,1000,50,10,1000,'LG',100)
e=Frigider(200,300,150,3000,20,30,4000,'Samsung',200)
g=Frigider(300,300,350,2000,70,30,6000,'Arctiv',500)
print(f,'\n',e,'\n',g,'\n')


Frigider.clasa=' <<Electrocasnice mari>>'
Frigider.subclasa='<<Frigider>>'
print('Valoarea atributelor de clasa')
print(Frigider.clasa)
print(Frigider.subclasa)

