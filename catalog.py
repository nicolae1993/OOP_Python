class Catalog:
    print('################### clasa CATALOG ##############')
    #class attribute with objects
    list=[]

    #variabile de clasa

    #clasa de echipamente
    clasa=''

    #sublasa de echipamente ex mixer
    subclasa=''


    #constructor
    def __init__(self,pret,consum,producator,cod_produs):
        self.pret=pret
        self.consum=consum
        self.producator=producator
        self.cod_produs=cod_produs

    def __str__(self):
        return str(self.pret)+" "+str(self.consum)+" "+str(self.producator)+" "+str(self.cod_produs)



a=Catalog(10,1000,'Michelin',100)
b=Catalog(20,2000,'Flanco',200)
c=Catalog(30,4000,'Emag',300)
d=Catalog(40,3000,'Ericsson',400)
e=Catalog(120,9000,'Flanco',300)
print('Afisarea instantelor de catalog :')
print(a,'\n',b,'\n',c,'\n',d,'\n',e,'\n')


Catalog.list.append(a)
Catalog.list.append(b)
Catalog.list.append(c)
Catalog.list.append(d)
Catalog.list.append(e)

'''
#afisarea obiectelor din lista
def printListCatalog(name):
    for x in name:
        print(x)
'''

#sortarea dupa pret
pret=[]
consum=[]

for p in Catalog.list:
    pret.append(p.pret)
    consum.append(p.consum)


#sa permita sortarea/filtrarea obiectelor din lista globala/variabila a clasei dupa pret
pret.sort()
print('Preturile sortate: ',pret)


#sa permita sortarea/filtrarea obiectelor din lista globala/variabila a clasei dupa consum

consum.sort()
print('Consumul sortat: ',consum)

# sa permita afisarea tuturor obiectelor de la un producator
# am ales Flanco ca producator de afisat

for x in Catalog.list:
    if(x.producator=='Flanco'):
        print('Instantele care au producatorul FLANCO : ',x)

print('\n','######################### SAU (o alta modalitate de afisare a instantelor dupa un anumit consumator )###################################')
def displayProducer(name):
    for x in Catalog.list:
        if(x.producator==name):
            print(x)
displayProducer('Flanco')