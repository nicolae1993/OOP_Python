from catalog import Catalog



class Electrocasnice_mici(Catalog):
    def __init__(self,lungime_cablu,baterie,pret,consum,producator,cod_produs):
        Catalog.__init__(self,pret,consum,producator,cod_produs)

        self.lungime_cablu=lungime_cablu
        self.baterie=baterie

    def __str__(self):
        return str(self.lungime_cablu)+" "+str(self.baterie)+" "+str(self.pret)+" "+str(self.consum)+" "+\
               str(self.producator)+" "+str(self.cod_produs)

print("Afisare electrocasnice MICI ############################")
em1=Electrocasnice_mici(4,'baterie_10',50,400,'Michelin',50)
em2=Electrocasnice_mici(3,'baterie_20',50,200,'Ericsson',510)
em3=Electrocasnice_mici(2,'baterie_30',30,100,'Emag',150)
print(em1)

