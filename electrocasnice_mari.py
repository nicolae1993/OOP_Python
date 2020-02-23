from catalog import Catalog

#__init__(self,pret,consum,producator,cod_produs) catalog class constructor

class Electrocasnice_mari(Catalog):
    def __init__(self,adancime,inaltime,latime,pret,consum,producator,cod_produs):
        super().__init__(pret,consum,producator,cod_produs)
        self.adancime=adancime
        self.inaltime=inaltime
        self.latime=latime

    def __str__(self):
         return str(self.adancime)+" "+str(self.inaltime)+" "+str(self.latime)+" "+str(self.pret)\
                +" "+str(self.consum)+" "+str(self.producator)+" "+str(self.cod_produs)



e=Electrocasnice_mari(100,1000,50,10,1000,'Michelin',100)
print('Electrocasnice',e)