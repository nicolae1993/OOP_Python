from electrocasnice_mari import Electrocasnice_mari


class Aragaz(Electrocasnice_mari):
    def __init__(self,nr_arzatoare,adancime,inaltime,latime,pret,consum,producator,cod_produs):
        self.nr_arzatoare=nr_arzatoare
        super().__init__(adancime,inaltime,latime,pret,consum,producator,cod_produs)

    def __str__(self):
         return str(self.adancime) + " " + str(self.inaltime) + " " + str(self.latime) + " " + str(self.pret) \
                 + " " + str(self.consum) + " " + str(self.producator) + " " + str(self.cod_produs) \
                 + " " + str(self.nr_arzatoare)

print('######### ARAGAZ ######################')
a=Aragaz(9,300,1090,20,19,1000,'Electrolux',150)
b=Aragaz(4,100,1200,30,15,1000,'Beko',300)
print(a)
print(b)
Aragaz.clasa='<Electrocasnice mari>>'
Aragaz.subclasa=' <<Aragaz>>'

print('Atributele clasei',Aragaz.clasa,Aragaz.subclasa)