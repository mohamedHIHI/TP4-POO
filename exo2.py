class Personne:
    def __init__(self,nom,age,adresse):
        self.__nom= nom
        self.__age= age
        self.__adresse= adresse

    def get_nom(self):
        return self.__nom
    def set_nom(self,nom):
          self.__nom = nom
    def get_age(self):
        return self.__age
    def set_age(self,age):
          self.__age = age
    def get_adresse(self):
        return self.__adresse
    def set_adresse(self,adresse):
         self.__adresse = adresse
    def afficher_information(self):
        print(self.get_nom(),self.get_age(),self.get_adresse())

class Etudiant(Personne):
    def __init__(self,nom,age,adresse,matricule,classe):
        super().__init__(nom,age,adresse)
        self.__matricule=matricule
        self.__classe=classe
    def afficher_information(self):
        print(self.get_nom(),self.get_age(),self.get_matricule(),self.get_matricule(),self.get_classe())
    def get_matricule(self):
        return self.__matricule
    def set_matricule(self,matricule):
          self.__matricule = matricule
    def get_classe(self):
        return self.__classe
    def set_classe(self,classe):
          self.__classe = classe
p=Personne("jack","56","sjsi,std,yhxus5 6354")
p.afficher_information()
e=Etudiant("yuif","45","khf hjyfcj hjuoyi","45646546","1")
e.afficher_information()

