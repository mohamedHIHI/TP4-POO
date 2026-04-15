class Employe:
    def __init__(self,nom,age,salaire):
        self.__nom= nom
        self.__age= age
        self.__salaire= salaire
    def get_nom(self):
        return self.__nom
    def set_nom(self,nom):
        self.__nom = nom
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
    def get_salaire(self):
        return self.__salaire
    def set_salaire(self,salaire):
        self.__salaire = salaire
    def afficher_information(self):
        print(self.get_nom(),self.get_age(),self.get_salaire())
class Manager(Employe):
    def __init__(self,nom,age,salaire,departement,subordonnes):
        super().__init__(self,nom,age,salaire)
        self.departement=departement
        self.subordonnes=subordonnes
    def get_departement(self):
        return self.departement
    def set_departement(self,departement):
        self.departement=departement
    def get_subordonnes(self):
        return self.subordonnes
    def set_subordonnes(self,subordonnes):
        self.subordonnes=subordonnes
    def ajouter_subordonne(self):
        print(self.get_nom(),self.get_age(),self.get_salaire(),self.get_departement(),self.get_subordonnes())
e=Employe("hgfyhj","44","10000")
e.afficher_information()
m=Manager("ilhy","55","10000","hfgdcjug","4554")
m.ajouter_subordonne()
