class Personne:
    def __init__(self,nom,age):
        self.__nom=nom
        self.__age=age
    def afficher_information(self):
        print(self.__nom,self.__age)
    def get_nom(self):
        return self.__nom
    def set_nom(self,nom):
        return self.__nom
    def get_age(self):
        return self.__age
    def set_age(self,age):
        return self.__age
class Employe(Personne):
   def __init__(self,nom,age,poste,salaire):
       super().__init__(nom,age)
       self.__poste=poste
       self.__salaire=salaire
   def afficher_information(self):
        print(self.__poste,self.__salaire)
   def get_poste(self):
       return self.__poste
   def set_poste(self,poste):
       return self.__poste
   def get_salaire(self):
       return self.__salaire
p=Personne("imane","20")
p.afficher_information()
p.get_nom()
p.get_age()
e=Employe("imane","20","rh","10000")
e.afficher_information()
e.get_poste()
e.get_salaire()








