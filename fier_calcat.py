import electrocasnice_mici

class Fier_calcat(electrocasnice_mici.Electrocasnice_mici):
    def __init__(self,rezervor,lungime_cablu,baterie,pret,consum,producator,cod_produs):
        self.rezervor=rezervor
        super().__init__(lungime_cablu,baterie,pret,consum,producator,cod_produs)

    def __str__(self):
        return  str(self.rezervor)+" "+str(self.lungime_cablu)+" "+str(self.baterie)+" "+str(self.pret)+" "+str(self.consum)+" "+\
               str(self.producator)+" "+str(self.cod_produs)

print("######################## FIER DE CALCAT ############################")
f=Fier_calcat('rezervor_100',4,'baterie_10',50,400,'Philips',50)
f2=Fier_calcat('rezervor_100',4,'baterie_10',50,400,'Elite',50)
print(f)
print(f2)
Fier_calcat.clasa=' <<Electrocasnice mici>>'
Fier_calcat.subclasa=' <<Fier calcat>>'
print(Fier_calcat.clasa)
print(Fier_calcat.subclasa)