from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen 
from random import choice
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import json
from kivy.uix.spinner import Spinner

class Mastermind(App) : 

    def build(self) : 

        #Gestion des différents écrans 

        self.__manager = ScreenManager()
        self.__manager.add_widget(self.buildScreen1())
        self.__manager.add_widget(self.buildScreen2())
        self.__manager.add_widget(self.buildScreen3())
        return self.__manager

    def buildScreen1(self) : 
        screen = Screen(name = "Screen1")

        self.title = "Mastermind"  

        #Composition aléatoire de 4 couleurs

        self.color1 = choice (["Bleu", "Vert", "Rouge", "Jaune", "Blanc", "Noir"])
        self.color2 = choice (["Bleu", "Vert", "Rouge", "Jaune", "Blanc", "Noir"])
        self.color3 = choice (["Bleu", "Vert", "Rouge", "Jaune", "Blanc", "Noir"])
        self.color4 = choice (["Bleu", "Vert", "Rouge", "Jaune", "Blanc", "Noir"])
        self.color = []
        self.color += [self.color1]
        self.color += [self.color2]
        self.color += [self.color3]
        self.color += [self.color4]
        self.double = {self.color[0], self.color[1], self.color[2], self.color[3]}

        #Affichage de la solution dans le terminal 

        print(self.color1, self.color2, self.color3, self.color4)

        #Création de la box principale 

        root = BoxLayout(orientation = "vertical")

        #Espacement

        self.spacing = 5
        self.padding = 5

        #Création de la première ligne 

        line1 = BoxLayout(orientation = "horizontal", size_hint = (1, (1/13)))

        self.labelNickname = Label(text = "Nickname : ", font_size = 25)
        self.inputNickname = TextInput(text = "", font_size = 25)
        self.buttonNickname = Button()
        self.buttonNickname.text = "Done"
        self.pointscore = 0
        self.labelBest = Label(text = "Best : " + str(self.bestscore()), font_size = 25)
        self.labelTentatives = Label(text = "Tentatives restantes : 10", font_size = 25)

        line1.add_widget(self.labelNickname)
        line1.add_widget(self.inputNickname)
        line1.add_widget(self.buttonNickname)
        line1.add_widget(self.labelBest)
        line1.add_widget(self.labelTentatives)

        root.add_widget(line1) 

        #Création de la deuxième ligne 

        line2 = BoxLayout(orientation = "horizontal", size_hint = (1, (1/13)))

        self.labelProposition = Label(text = "Propositions",size_hint = ((2/3), 1), font_size = 25)
        self.labelOk = Label(text = "Ok", size_hint = ((1/6), 1), font_size = 25)
        self.labelColor = Label(text = "Color", size_hint = ((1/6), 1), font_size = 25)

        line2.add_widget(self.labelProposition)
        line2.add_widget(self.labelOk)
        line2.add_widget(self.labelColor)

        root.add_widget(line2)

        #Création de la troisième ligne 

        line3 = BoxLayout(orientation = "vertical", size_hint = (1, (10/13)))

        line4 = BoxLayout(orientation = "horizontal")
        
        self.labeloutput41 = Label(text = "", font_size = 25) 
        self.labeloutput42 = Label(text = "", font_size = 25)
        self.labeloutput43 = Label(text = "", font_size = 25)
        self.labeloutput44 = Label(text = "", font_size = 25)
        self.labeloutput45 = Label(text = "", font_size = 25)
        self.labeloutput46 = Label(text = "", font_size = 25)

        line4.add_widget(self.labeloutput41)
        line4.add_widget(self.labeloutput42)
        line4.add_widget(self.labeloutput43)
        line4.add_widget(self.labeloutput44)
        line4.add_widget(self.labeloutput45)
        line4.add_widget(self.labeloutput46)

        line3.add_widget(line4)

        line5 = BoxLayout(orientation = "horizontal")

        self.labeloutput51 = Label(text = "", font_size = 25) 
        self.labeloutput52 = Label(text = "", font_size = 25)
        self.labeloutput53 = Label(text = "", font_size = 25)
        self.labeloutput54 = Label(text = "", font_size = 25)
        self.labeloutput55 = Label(text = "", font_size = 25)
        self.labeloutput56 = Label(text = "", font_size = 25)

        line5.add_widget(self.labeloutput51)
        line5.add_widget(self.labeloutput52)
        line5.add_widget(self.labeloutput53)
        line5.add_widget(self.labeloutput54)
        line5.add_widget(self.labeloutput55)
        line5.add_widget(self.labeloutput56)

        line3.add_widget(line5)

        line6 = BoxLayout(orientation = "horizontal")

        self.labeloutput61 = Label(text = "", font_size = 25) 
        self.labeloutput62 = Label(text = "", font_size = 25)
        self.labeloutput63 = Label(text = "", font_size = 25)
        self.labeloutput64 = Label(text = "", font_size = 25)
        self.labeloutput65 = Label(text = "", font_size = 25)
        self.labeloutput66 = Label(text = "", font_size = 25)

        line6.add_widget(self.labeloutput61)
        line6.add_widget(self.labeloutput62)
        line6.add_widget(self.labeloutput63)
        line6.add_widget(self.labeloutput64)
        line6.add_widget(self.labeloutput65)
        line6.add_widget(self.labeloutput66)

        line3.add_widget(line6)

        line7 = BoxLayout(orientation = "horizontal")

        self.labeloutput71 = Label(text = "", font_size = 25) 
        self.labeloutput72 = Label(text = "", font_size = 25)
        self.labeloutput73 = Label(text = "", font_size = 25)
        self.labeloutput74 = Label(text = "", font_size = 25)
        self.labeloutput75 = Label(text = "", font_size = 25)
        self.labeloutput76 = Label(text = "", font_size = 25)

        line7.add_widget(self.labeloutput71)
        line7.add_widget(self.labeloutput72)
        line7.add_widget(self.labeloutput73)
        line7.add_widget(self.labeloutput74)
        line7.add_widget(self.labeloutput75)
        line7.add_widget(self.labeloutput76)

        line3.add_widget(line7)

        line8 = BoxLayout(orientation = "horizontal")

        self.labeloutput81 = Label(text = "", font_size = 25) 
        self.labeloutput82 = Label(text = "", font_size = 25)
        self.labeloutput83 = Label(text = "", font_size = 25)
        self.labeloutput84 = Label(text = "", font_size = 25)
        self.labeloutput85 = Label(text = "", font_size = 25)
        self.labeloutput86 = Label(text = "", font_size = 25)

        line8.add_widget(self.labeloutput81)
        line8.add_widget(self.labeloutput82)
        line8.add_widget(self.labeloutput83)
        line8.add_widget(self.labeloutput84)
        line8.add_widget(self.labeloutput85)
        line8.add_widget(self.labeloutput86)

        line3.add_widget(line8)

        line9 = BoxLayout(orientation = "horizontal")

        self.labeloutput91 = Label(text = "", font_size = 25) 
        self.labeloutput92 = Label(text = "", font_size = 25)
        self.labeloutput93 = Label(text = "", font_size = 25)
        self.labeloutput94 = Label(text = "", font_size = 25)
        self.labeloutput95 = Label(text = "", font_size = 25)
        self.labeloutput96 = Label(text = "", font_size = 25)

        line9.add_widget(self.labeloutput91)
        line9.add_widget(self.labeloutput92)
        line9.add_widget(self.labeloutput93)
        line9.add_widget(self.labeloutput94)
        line9.add_widget(self.labeloutput95)
        line9.add_widget(self.labeloutput96)

        line3.add_widget(line9)

        line10 = BoxLayout(orientation = "horizontal")

        self.labeloutput101 = Label(text = "", font_size = 25) 
        self.labeloutput102 = Label(text = "", font_size = 25)
        self.labeloutput103 = Label(text = "", font_size = 25)
        self.labeloutput104 = Label(text = "", font_size = 25)
        self.labeloutput105 = Label(text = "", font_size = 25)
        self.labeloutput106 = Label(text = "", font_size = 25)

        line10.add_widget(self.labeloutput101)
        line10.add_widget(self.labeloutput102)
        line10.add_widget(self.labeloutput103)
        line10.add_widget(self.labeloutput104)
        line10.add_widget(self.labeloutput105)
        line10.add_widget(self.labeloutput106)

        line3.add_widget(line10)

        line11 = BoxLayout(orientation = "horizontal")

        self.labeloutput111 = Label(text = "", font_size = 25) 
        self.labeloutput112 = Label(text = "", font_size = 25)
        self.labeloutput113 = Label(text = "", font_size = 25)
        self.labeloutput114 = Label(text = "", font_size = 25)
        self.labeloutput115 = Label(text = "", font_size = 25)
        self.labeloutput116 = Label(text = "", font_size = 25)

        line11.add_widget(self.labeloutput111)
        line11.add_widget(self.labeloutput112)
        line11.add_widget(self.labeloutput113)
        line11.add_widget(self.labeloutput114)
        line11.add_widget(self.labeloutput115)
        line11.add_widget(self.labeloutput116)

        line3.add_widget(line11)

        line12 = BoxLayout(orientation = "horizontal")

        self.labeloutput121 = Label(text = "", font_size = 25) 
        self.labeloutput122 = Label(text = "", font_size = 25)
        self.labeloutput123 = Label(text = "", font_size = 25)
        self.labeloutput124 = Label(text = "", font_size = 25)
        self.labeloutput125 = Label(text = "", font_size = 25)
        self.labeloutput126 = Label(text = "", font_size = 25)

        line12.add_widget(self.labeloutput121)
        line12.add_widget(self.labeloutput122)
        line12.add_widget(self.labeloutput123)
        line12.add_widget(self.labeloutput124)
        line12.add_widget(self.labeloutput125)
        line12.add_widget(self.labeloutput126)

        line3.add_widget(line12)

        line13 = BoxLayout(orientation = "horizontal")

        self.labeloutput131 = Label(text = "", font_size = 25) 
        self.labeloutput132 = Label(text = "", font_size = 25)
        self.labeloutput133 = Label(text = "", font_size = 25)
        self.labeloutput134 = Label(text = "", font_size = 25)
        self.labeloutput135 = Label(text = "", font_size = 25)
        self.labeloutput136 = Label(text = "", font_size = 25)

        line13.add_widget(self.labeloutput131)
        line13.add_widget(self.labeloutput132)
        line13.add_widget(self.labeloutput133)
        line13.add_widget(self.labeloutput134)
        line13.add_widget(self.labeloutput135)
        line13.add_widget(self.labeloutput136)

        line3.add_widget(line13)

        root.add_widget(line3)

        #Création de la dernière ligne 

        line14 = BoxLayout(orientation = "horizontal", size_hint = (1, (1/13))) 
        self.spinner1 = Spinner(text = "Couleur", values = ("Bleu", "Vert", "Rouge", "Jaune", "Blanc", "Noir"), font_size = 25)
        self.spinner2 = Spinner(text = "Couleur", values = ("Bleu", "Vert", "Rouge", "Jaune", "Blanc", "Noir"), font_size = 25)
        self.spinner3 = Spinner(text = "Couleur", values = ("Bleu", "Vert", "Rouge", "Jaune", "Blanc", "Noir"), font_size = 25)
        self.spinner4 = Spinner(text = "Couleur", values = ("Bleu", "Vert", "Rouge", "Jaune", "Blanc", "Noir"), font_size = 25)
        self.buttonColor = Button(font_size = 25)
        self.buttonColor.text = "Ok"
        self.buttonColor.background_color = [1, 0, 1, 1]
        self.buttonColor.bind(on_press = self.compute)
        
        line14.add_widget(self.spinner1)
        line14.add_widget(self.spinner2)
        line14.add_widget(self.spinner3)
        line14.add_widget(self.spinner4)
        line14.add_widget(self.buttonColor)

        root.add_widget(line14) 

        screen.add_widget(root) 

        return screen

    #Fonction pour numériser le meilleur score de chaque joueur 

    def bestscore(self) : 
        try : 
            with open("Partie.json") as file : 
                Partie = json.loads(file.read())
        except FileNotFoundError : 
            Partie = {}
        for elem in Partie : 
            if Partie[elem]["Point du joueur"] > self.pointscore : 
                self.pointscore = Partie[elem]["Point du joueur"]
        return "{} points".format(str(self.pointscore)) 

    #Fonction qui permet de sauvegarder les résultats des différents joueurs

    def best(self) :
        try:
            with open("Partie.json") as file:
                Partie = json.loads(file.read())
        except FileNotFoundError:
            Partie = {}

        partie = len(Partie) + 1
        Partie["Partie {}".format(partie)] = {"Nom" : self.inputNickname.text, "Point du joueur" : self.pointscore}

        with open("Partie.json", "w") as file:
            file.write(json.dumps(Partie, indent = '\t'))

    #Fonction qui permet de gérer le deuxième écran

    def buildScreen2(self) : 
        screen = Screen(name = "Screen2")
        self.labelWin = Label(text = "Vous avez gagné :)", font_size = 100, color = [0, 1, 0, 1])
        screen.add_widget(self.labelWin) 
        return screen

    #Fonction qui permet de gérer le troisième écran

    def buildScreen3(self) : 
        screen = Screen(name = "Screen3")
        
        root = BoxLayout(orientation = "vertical") 

        line1 = BoxLayout(orientation = "horizontal")
        line2 = BoxLayout(orientation = "horizontal")

        self.labelLose = Label(text = "Vous avez perdu :(", font_size = 100, color = [1, 0, 0, 1]) 
        self.labelSolution = Label(text = "La proposition correcte était :  {}".format(self.solution()), font_size = 50)

        line1.add_widget(self.labelLose)
        line2.add_widget(self.labelSolution)

        root.add_widget(line1) 
        root.add_widget(line2) 

        screen.add_widget(root) 

        return screen 

    #Fonction qui pemret d'afficher la proposition correcte en cas de défaite 

    def solution(self) : 
        return str(self.color1) + "  " + str(self.color2) + "  " +  str(self.color3) + "  " + str(self.color4)

    #Fonction qui permet de donner le résultat d'une proposition encodée 

    def compute(self, source) : 
        
        #Tentative 1 

        if self.labeloutput41.text == "" : 

            #Affichage du nombre de tentatives restantes 

            self.labelTentatives.text = "Tentatives restantes : 9"

            #Encoder la proposition 
            
            self.labeloutput41.text = self.spinner1.text
            if self.labeloutput41.text == "Bleu" : 
                self.labeloutput41.color = [0, 0, 1, 1]
            if self.labeloutput41.text == "Vert" : 
                self.labeloutput41.color = [0, 1, 0, 1]
            if self.labeloutput41.text == "Rouge" : 
                self.labeloutput41.color = [1, 0, 0, 1]
            if self.labeloutput41.text == "Jaune" : 
                self.labeloutput41.color = [1, 1, 0, 1]
            
            self.labeloutput42.text = self.spinner2.text
            if self.labeloutput42.text == "Bleu" : 
                self.labeloutput42.color = [0, 0, 1, 1]
            if self.labeloutput42.text == "Vert" : 
                self.labeloutput42.color = [0, 1, 0, 1]
            if self.labeloutput42.text == "Rouge" : 
                self.labeloutput42.color = [1, 0, 0, 1]
            if self.labeloutput42.text == "Jaune" : 
                self.labeloutput42.color = [1, 1, 0, 1]

            self.labeloutput43.text = self.spinner3.text
            if self.labeloutput43.text == "Bleu" : 
                self.labeloutput43.color = [0, 0, 1, 1]
            if self.labeloutput43.text == "Vert" : 
                self.labeloutput43.color = [0, 1, 0, 1]
            if self.labeloutput43.text == "Rouge" : 
                self.labeloutput43.color = [1, 0, 0, 1]
            if self.labeloutput43.text == "Jaune" : 
                self.labeloutput43.color = [1, 1, 0, 1]

            self.labeloutput44.text = self.spinner4.text
            if self.labeloutput44.text == "Bleu" : 
                self.labeloutput44.color = [0, 0, 1, 1]
            if self.labeloutput44.text == "Vert" : 
                self.labeloutput44.color = [0, 1, 0, 1]
            if self.labeloutput44.text == "Rouge" : 
                self.labeloutput44.color = [1, 0, 0, 1]
            if self.labeloutput44.text == "Jaune" : 
                self.labeloutput44.color = [1, 1, 0, 1]

            #Affichage du nombre de bonnes couleurs bien placées (Ok) 
            
            count0 = 0 
            if self.color[0] == self.spinner1.text : 
                count0 = count0 + 1
            if self.color[1] == self.spinner2.text : 
                count0 = count0 + 1
            if self.color[2] == self.spinner3.text : 
                count0 = count0 + 1
            if self.color[3] == self.spinner4.text : 
                count0 = count0 + 1
            self.labeloutput45.text = str(count0) 

            #Affichage si le joueur à gagné 

            if count0 == 4 : 
                self.pointscore = 10
                self.best()
                self.WinScreen2() 

            #Affichage du nombre de bonnes couleurs (Color)

            count1 = 0 
            elem = 0
            for elem in self.double : 
                if elem in self.double : 
                    if elem in self.spinner1.text : 
                        count1 = count1 + 1
                    elif elem in self.spinner2.text : 
                        count1 = count1 + 1
                    elif elem in self.spinner3.text : 
                        count1 = count1 + 1
                    elif elem in self.spinner4.text : 
                        count1 = count1 + 1
            self.labeloutput46.text = str(count1)

        #Tentative 2 

        elif self.labeloutput41.text != "" and self.labeloutput51.text == "" : 

            #Affichage du nombre de tentatives restantes 

            self.labelTentatives.text = "Tentatives restantes : 8"

            #Encoder la proposition 
            
            self.labeloutput51.text = self.spinner1.text
            if self.labeloutput51.text == "Bleu" : 
                self.labeloutput51.color = [0, 0, 1, 1]
            if self.labeloutput51.text == "Vert" : 
                self.labeloutput51.color = [0, 1, 0, 1]
            if self.labeloutput51.text == "Rouge" : 
                self.labeloutput51.color = [1, 0, 0, 1]
            if self.labeloutput51.text == "Jaune" : 
                self.labeloutput51.color = [1, 1, 0, 1]
            
            self.labeloutput52.text = self.spinner2.text
            if self.labeloutput52.text == "Bleu" : 
                self.labeloutput52.color = [0, 0, 1, 1]
            if self.labeloutput52.text == "Vert" : 
                self.labeloutput52.color = [0, 1, 0, 1]
            if self.labeloutput52.text == "Rouge" : 
                self.labeloutput52.color = [1, 0, 0, 1]
            if self.labeloutput52.text == "Jaune" : 
                self.labeloutput52.color = [1, 1, 0, 1]

            self.labeloutput53.text = self.spinner3.text
            if self.labeloutput53.text == "Bleu" : 
                self.labeloutput53.color = [0, 0, 1, 1]
            if self.labeloutput53.text == "Vert" : 
                self.labeloutput53.color = [0, 1, 0, 1]
            if self.labeloutput53.text == "Rouge" : 
                self.labeloutput53.color = [1, 0, 0, 1]
            if self.labeloutput53.text == "Jaune" : 
                self.labeloutput53.color = [1, 1, 0, 1]

            self.labeloutput54.text = self.spinner4.text
            if self.labeloutput54.text == "Bleu" : 
                self.labeloutput54.color = [0, 0, 1, 1]
            if self.labeloutput54.text == "Vert" : 
                self.labeloutput54.color = [0, 1, 0, 1]
            if self.labeloutput54.text == "Rouge" : 
                self.labeloutput54.color = [1, 0, 0, 1]
            if self.labeloutput54.text == "Jaune" : 
                self.labeloutput54.color = [1, 1, 0, 1]

            #Affichage du nombre de bonnes couleurs bien placées (Ok) 
            
            count2 = 0 
            if self.color[0] == self.spinner1.text : 
                count2 = count2 + 1
            if self.color[1] == self.spinner2.text : 
                count2 = count2 + 1
            if self.color[2] == self.spinner3.text : 
                count2 = count2 + 1
            if self.color[3] == self.spinner4.text : 
                count2 = count2 + 1
            self.labeloutput55.text = str(count2) 

            #Affichage si le joueur à gagné 

            if count2 == 4 : 
                self.pointscore = 9
                self.best()
                self.WinScreen2() 

            #Affichage du nombre de bonnes couleurs (Color)

            count3 = 0 
            elem = 0
            for elem in self.double : 
                if elem in self.double : 
                    if elem in self.spinner1.text : 
                        count3 = count3 + 1
                    elif elem in self.spinner2.text : 
                        count3 = count3 + 1
                    elif elem in self.spinner3.text : 
                        count3 = count3 + 1
                    elif elem in self.spinner4.text : 
                        count3 = count3 + 1
            self.labeloutput56.text = str(count3) 

        #Tentative 3 

        elif self.labeloutput51.text != "" and self.labeloutput61.text == "" : 

            #Affichage du nombre de tentatives restantes 

            self.labelTentatives.text = "Tentatives restantes : 7"

            #Encoder la proposition 
            
            self.labeloutput61.text = self.spinner1.text
            if self.labeloutput61.text == "Bleu" : 
                self.labeloutput61.color = [0, 0, 1, 1]
            if self.labeloutput61.text == "Vert" : 
                self.labeloutput61.color = [0, 1, 0, 1]
            if self.labeloutput61.text == "Rouge" : 
                self.labeloutput61.color = [1, 0, 0, 1]
            if self.labeloutput61.text == "Jaune" : 
                self.labeloutput61.color = [1, 1, 0, 1]
            
            self.labeloutput62.text = self.spinner2.text
            if self.labeloutput62.text == "Bleu" : 
                self.labeloutput62.color = [0, 0, 1, 1]
            if self.labeloutput62.text == "Vert" : 
                self.labeloutput62.color = [0, 1, 0, 1]
            if self.labeloutput62.text == "Rouge" : 
                self.labeloutput62.color = [1, 0, 0, 1]
            if self.labeloutput62.text == "Jaune" : 
                self.labeloutput62.color = [1, 1, 0, 1]

            self.labeloutput63.text = self.spinner3.text
            if self.labeloutput63.text == "Bleu" : 
                self.labeloutput63.color = [0, 0, 1, 1]
            if self.labeloutput63.text == "Vert" : 
                self.labeloutput63.color = [0, 1, 0, 1]
            if self.labeloutput63.text == "Rouge" : 
                self.labeloutput63.color = [1, 0, 0, 1]
            if self.labeloutput63.text == "Jaune" : 
                self.labeloutput63.color = [1, 1, 0, 1]

            self.labeloutput64.text = self.spinner4.text
            if self.labeloutput64.text == "Bleu" : 
                self.labeloutput64.color = [0, 0, 1, 1]
            if self.labeloutput64.text == "Vert" : 
                self.labeloutput64.color = [0, 1, 0, 1]
            if self.labeloutput64.text == "Rouge" : 
                self.labeloutput64.color = [1, 0, 0, 1]
            if self.labeloutput64.text == "Jaune" : 
                self.labeloutput64.color = [1, 1, 0, 1]

            #Affichage du nombre de bonnes couleurs bien placées (Ok) 
            
            count4 = 0 
            if self.color[0] == self.spinner1.text : 
                count4 = count4 + 1
            if self.color[1] == self.spinner2.text : 
                count4 = count4 + 1
            if self.color[2] == self.spinner3.text : 
                count4 = count4 + 1
            if self.color[3] == self.spinner4.text : 
                count4 = count4 + 1
            self.labeloutput65.text = str(count4) 

            #Affichage si le joueur à gagné 

            if count4 == 4 : 
                self.pointscore = 8
                self.best()
                self.WinScreen2() 

            #Affichage du nombre de bonnes couleurs (Color)

            count5 = 0 
            elem = 0
            for elem in self.double : 
                if elem in self.double : 
                    if elem in self.spinner1.text : 
                        count5 = count5 + 1
                    elif elem in self.spinner2.text : 
                        count5 = count5 + 1
                    elif elem in self.spinner3.text : 
                        count5 = count5 + 1
                    elif elem in self.spinner4.text : 
                        count5 = count5 + 1
            self.labeloutput66.text = str(count5)

        #Tentative 4 

        elif self.labeloutput61.text != "" and self.labeloutput71.text == "" : 

            #Affichage du nombre de tentatives restantes 

            self.labelTentatives.text = "Tentatives restantes : 6"

            #Encoder la proposition 
            
            self.labeloutput71.text = self.spinner1.text
            if self.labeloutput71.text == "Bleu" : 
                self.labeloutput71.color = [0, 0, 1, 1]
            if self.labeloutput71.text == "Vert" : 
                self.labeloutput71.color = [0, 1, 0, 1]
            if self.labeloutput71.text == "Rouge" : 
                self.labeloutput71.color = [1, 0, 0, 1]
            if self.labeloutput71.text == "Jaune" : 
                self.labeloutput71.color = [1, 1, 0, 1]
            
            self.labeloutput72.text = self.spinner2.text
            if self.labeloutput72.text == "Bleu" : 
                self.labeloutput72.color = [0, 0, 1, 1]
            if self.labeloutput72.text == "Vert" : 
                self.labeloutput72.color = [0, 1, 0, 1]
            if self.labeloutput72.text == "Rouge" : 
                self.labeloutput72.color = [1, 0, 0, 1]
            if self.labeloutput72.text == "Jaune" : 
                self.labeloutput72.color = [1, 1, 0, 1]

            self.labeloutput73.text = self.spinner3.text
            if self.labeloutput73.text == "Bleu" : 
                self.labeloutput73.color = [0, 0, 1, 1]
            if self.labeloutput73.text == "Vert" : 
                self.labeloutput73.color = [0, 1, 0, 1]
            if self.labeloutput73.text == "Rouge" : 
                self.labeloutput73.color = [1, 0, 0, 1]
            if self.labeloutput73.text == "Jaune" : 
                self.labeloutput73.color = [1, 1, 0, 1]

            self.labeloutput74.text = self.spinner4.text
            if self.labeloutput74.text == "Bleu" : 
                self.labeloutput74.color = [0, 0, 1, 1]
            if self.labeloutput74.text == "Vert" : 
                self.labeloutput74.color = [0, 1, 0, 1]
            if self.labeloutput74.text == "Rouge" : 
                self.labeloutput74.color = [1, 0, 0, 1]
            if self.labeloutput74.text == "Jaune" : 
                self.labeloutput74.color = [1, 1, 0, 1]

            #Affichage du nombre de bonnes couleurs bien placées (Ok) 
            
            count6 = 0 
            if self.color[0] == self.spinner1.text : 
                count6 = count6 + 1
            if self.color[1] == self.spinner2.text : 
                count6 = count6 + 1
            if self.color[2] == self.spinner3.text : 
                count6 = count6 + 1
            if self.color[3] == self.spinner4.text : 
                count6 = count6 + 1
            self.labeloutput75.text = str(count6) 

            #Affichage si le joueur à gagné 

            if count6 == 4 : 
                self.pointscore = 7
                self.best()
                self.WinScreen2() 

            #Affichage du nombre de bonnes couleurs (Color)

            count7 = 0 
            elem = 0
            for elem in self.double : 
                if elem in self.double : 
                    if elem in self.spinner1.text : 
                        count7 = count7 + 1
                    elif elem in self.spinner2.text : 
                        count7 = count7 + 1
                    elif elem in self.spinner3.text : 
                        count7 = count7 + 1
                    elif elem in self.spinner4.text : 
                        count7 = count7 + 1
            self.labeloutput76.text = str(count7)

        #Tentative 5 

        elif self.labeloutput71.text != "" and self.labeloutput81.text == "" : 

            #Affichage du nombre de tentatives restantes 

            self.labelTentatives.text = "Tentatives restantes : 5"

            #Encoder la proposition 
            
            self.labeloutput81.text = self.spinner1.text
            if self.labeloutput81.text == "Bleu" : 
                self.labeloutput81.color = [0, 0, 1, 1]
            if self.labeloutput81.text == "Vert" : 
                self.labeloutput81.color = [0, 1, 0, 1]
            if self.labeloutput81.text == "Rouge" : 
                self.labeloutput81.color = [1, 0, 0, 1]
            if self.labeloutput81.text == "Jaune" : 
                self.labeloutput81.color = [1, 1, 0, 1]
            
            self.labeloutput82.text = self.spinner2.text
            if self.labeloutput82.text == "Bleu" : 
                self.labeloutput82.color = [0, 0, 1, 1]
            if self.labeloutput82.text == "Vert" : 
                self.labeloutput82.color = [0, 1, 0, 1]
            if self.labeloutput82.text == "Rouge" : 
                self.labeloutput82.color = [1, 0, 0, 1]
            if self.labeloutput82.text == "Jaune" : 
                self.labeloutput82.color = [1, 1, 0, 1]

            self.labeloutput83.text = self.spinner3.text
            if self.labeloutput83.text == "Bleu" : 
                self.labeloutput83.color = [0, 0, 1, 1]
            if self.labeloutput83.text == "Vert" : 
                self.labeloutput83.color = [0, 1, 0, 1]
            if self.labeloutput83.text == "Rouge" : 
                self.labeloutput83.color = [1, 0, 0, 1]
            if self.labeloutput83.text == "Jaune" : 
                self.labeloutput83.color = [1, 1, 0, 1]

            self.labeloutput84.text = self.spinner4.text
            if self.labeloutput84.text == "Bleu" : 
                self.labeloutput84.color = [0, 0, 1, 1]
            if self.labeloutput84.text == "Vert" : 
                self.labeloutput84.color = [0, 1, 0, 1]
            if self.labeloutput84.text == "Rouge" : 
                self.labeloutput84.color = [1, 0, 0, 1]
            if self.labeloutput84.text == "Jaune" : 
                self.labeloutput84.color = [1, 1, 0, 1]

            #Affichage du nombre de bonnes couleurs bien placées (Ok) 
            
            count8 = 0 
            if self.color[0] == self.spinner1.text : 
                count8 = count8 + 1
            if self.color[1] == self.spinner2.text : 
                count8 = count8 + 1
            if self.color[2] == self.spinner3.text : 
                count8 = count8 + 1
            if self.color[3] == self.spinner4.text : 
                count8 = count8 + 1
            self.labeloutput85.text = str(count8) 

            #Affichage si le joueur à gagné 

            if count8 == 4 : 
                self.pointscore = 6
                self.best()
                self.WinScreen2() 

            #Affichage du nombre de bonnes couleurs (Color)

            count9 = 0 
            elem = 0
            for elem in self.double : 
                if elem in self.double : 
                    if elem in self.spinner1.text : 
                        count9 = count9 + 1
                    elif elem in self.spinner2.text : 
                        count9 = count9 + 1
                    elif elem in self.spinner3.text : 
                        count9 = count9 + 1
                    elif elem in self.spinner4.text : 
                        count9 = count9 + 1
            self.labeloutput86.text = str(count9)

        #Tentative 6 

        elif self.labeloutput81.text != "" and self.labeloutput91.text == "" : 

            #Affichage du nombre de tentatives restantes 

            self.labelTentatives.text = "Tentatives restantes : 4"

            #Encoder la proposition 
            
            self.labeloutput91.text = self.spinner1.text
            if self.labeloutput91.text == "Bleu" : 
                self.labeloutput91.color = [0, 0, 1, 1]
            if self.labeloutput91.text == "Vert" : 
                self.labeloutput91.color = [0, 1, 0, 1]
            if self.labeloutput91.text == "Rouge" : 
                self.labeloutput91.color = [1, 0, 0, 1]
            if self.labeloutput91.text == "Jaune" : 
                self.labeloutput91.color = [1, 1, 0, 1]
            
            self.labeloutput92.text = self.spinner2.text
            if self.labeloutput92.text == "Bleu" : 
                self.labeloutput92.color = [0, 0, 1, 1]
            if self.labeloutput92.text == "Vert" : 
                self.labeloutput92.color = [0, 1, 0, 1]
            if self.labeloutput92.text == "Rouge" : 
                self.labeloutput92.color = [1, 0, 0, 1]
            if self.labeloutput92.text == "Jaune" : 
                self.labeloutput92.color = [1, 1, 0, 1]

            self.labeloutput93.text = self.spinner3.text
            if self.labeloutput93.text == "Bleu" : 
                self.labeloutput93.color = [0, 0, 1, 1]
            if self.labeloutput93.text == "Vert" : 
                self.labeloutput93.color = [0, 1, 0, 1]
            if self.labeloutput93.text == "Rouge" : 
                self.labeloutput93.color = [1, 0, 0, 1]
            if self.labeloutput93.text == "Jaune" : 
                self.labeloutput93.color = [1, 1, 0, 1]

            self.labeloutput94.text = self.spinner4.text
            if self.labeloutput94.text == "Bleu" : 
                self.labeloutput94.color = [0, 0, 1, 1]
            if self.labeloutput94.text == "Vert" : 
                self.labeloutput94.color = [0, 1, 0, 1]
            if self.labeloutput94.text == "Rouge" : 
                self.labeloutput94.color = [1, 0, 0, 1]
            if self.labeloutput94.text == "Jaune" : 
                self.labeloutput94.color = [1, 1, 0, 1]

            #Affichage du nombre de bonnes couleurs bien placées (Ok) 
            
            count10 = 0 
            if self.color[0] == self.spinner1.text : 
                count10 = count10 + 1
            if self.color[1] == self.spinner2.text : 
                count10 = count10 + 1
            if self.color[2] == self.spinner3.text : 
                count10 = count10 + 1
            if self.color[3] == self.spinner4.text : 
                count10 = count10 + 1
            self.labeloutput95.text = str(count10) 

            #Affichage si le joueur à gagné 

            if count10 == 4 : 
                self.pointscore = 5
                self.best()
                self.WinScreen2() 

            #Affichage du nombre de bonnes couleurs (Color)

            count11 = 0 
            elem = 0
            for elem in self.double : 
                if elem in self.double : 
                    if elem in self.spinner1.text : 
                        count11 = count11 + 1
                    elif elem in self.spinner2.text : 
                        count11 = count11 + 1
                    elif elem in self.spinner3.text : 
                        count11 = count11 + 1
                    elif elem in self.spinner4.text : 
                        count11 = count11 + 1
            self.labeloutput96.text = str(count11)

        #Tentative 7 

        elif self.labeloutput91.text != "" and self.labeloutput101.text == "" : 

            #Affichage du nombre de tentatives restantes 

            self.labelTentatives.text = "Tentatives restantes : 3"

            #Encoder la proposition 
            
            self.labeloutput101.text = self.spinner1.text
            if self.labeloutput101.text == "Bleu" : 
                self.labeloutput101.color = [0, 0, 1, 1]
            if self.labeloutput101.text == "Vert" : 
                self.labeloutput101.color = [0, 1, 0, 1]
            if self.labeloutput101.text == "Rouge" : 
                self.labeloutput101.color = [1, 0, 0, 1]
            if self.labeloutput101.text == "Jaune" : 
                self.labeloutput101.color = [1, 1, 0, 1]
            
            self.labeloutput102.text = self.spinner2.text
            if self.labeloutput102.text == "Bleu" : 
                self.labeloutput102.color = [0, 0, 1, 1]
            if self.labeloutput102.text == "Vert" : 
                self.labeloutput102.color = [0, 1, 0, 1]
            if self.labeloutput102.text == "Rouge" : 
                self.labeloutput102.color = [1, 0, 0, 1]
            if self.labeloutput102.text == "Jaune" : 
                self.labeloutput102.color = [1, 1, 0, 1]

            self.labeloutput103.text = self.spinner3.text
            if self.labeloutput103.text == "Bleu" : 
                self.labeloutput103.color = [0, 0, 1, 1]
            if self.labeloutput103.text == "Vert" : 
                self.labeloutput103.color = [0, 1, 0, 1]
            if self.labeloutput103.text == "Rouge" : 
                self.labeloutput103.color = [1, 0, 0, 1]
            if self.labeloutput103.text == "Jaune" : 
                self.labeloutput103.color = [1, 1, 0, 1]

            self.labeloutput104.text = self.spinner4.text
            if self.labeloutput104.text == "Bleu" : 
                self.labeloutput104.color = [0, 0, 1, 1]
            if self.labeloutput104.text == "Vert" : 
                self.labeloutput104.color = [0, 1, 0, 1]
            if self.labeloutput104.text == "Rouge" : 
                self.labeloutput104.color = [1, 0, 0, 1]
            if self.labeloutput104.text == "Jaune" : 
                self.labeloutput104.color = [1, 1, 0, 1]

            #Affichage du nombre de bonnes couleurs bien placées (Ok) 
            
            count12 = 0 
            if self.color[0] == self.spinner1.text : 
                count12 = count12 + 1
            if self.color[1] == self.spinner2.text : 
                count12 = count12 + 1
            if self.color[2] == self.spinner3.text : 
                count12 = count12 + 1
            if self.color[3] == self.spinner4.text : 
                count12 = count12 + 1
            self.labeloutput105.text = str(count12) 

            #Affichage si le joueur à gagné 

            if count12 == 4 : 
                self.pointscore = 4
                self.best()
                self.WinScreen2() 

            #Affichage du nombre de bonnes couleurs (Color)

            count13 = 0 
            elem = 0
            for elem in self.double : 
                if elem in self.double : 
                    if elem in self.spinner1.text : 
                        count13 = count13 + 1
                    elif elem in self.spinner2.text : 
                        count13 = count13 + 1
                    elif elem in self.spinner3.text : 
                        count13 = count13 + 1
                    elif elem in self.spinner4.text : 
                        count13 = count13 + 1
            self.labeloutput106.text = str(count13)

        #Tentative 8 

        elif self.labeloutput101.text != "" and self.labeloutput111.text == "" : 

            #Affichage du nombre de tentatives restantes 

            self.labelTentatives.text = "Tentatives restantes : 2"

            #Encoder la proposition 
            
            self.labeloutput111.text = self.spinner1.text
            if self.labeloutput111.text == "Bleu" : 
                self.labeloutput111.color = [0, 0, 1, 1]
            if self.labeloutput111.text == "Vert" : 
                self.labeloutput111.color = [0, 1, 0, 1]
            if self.labeloutput111.text == "Rouge" : 
                self.labeloutput111.color = [1, 0, 0, 1]
            if self.labeloutput111.text == "Jaune" : 
                self.labeloutput111.color = [1, 1, 0, 1]
            
            self.labeloutput112.text = self.spinner2.text
            if self.labeloutput112.text == "Bleu" : 
                self.labeloutput112.color = [0, 0, 1, 1]
            if self.labeloutput112.text == "Vert" : 
                self.labeloutput112.color = [0, 1, 0, 1]
            if self.labeloutput112.text == "Rouge" : 
                self.labeloutput112.color = [1, 0, 0, 1]
            if self.labeloutput112.text == "Jaune" : 
                self.labeloutput112.color = [1, 1, 0, 1]

            self.labeloutput113.text = self.spinner3.text
            if self.labeloutput113.text == "Bleu" : 
                self.labeloutput113.color = [0, 0, 1, 1]
            if self.labeloutput113.text == "Vert" : 
                self.labeloutput113.color = [0, 1, 0, 1]
            if self.labeloutput113.text == "Rouge" : 
                self.labeloutput113.color = [1, 0, 0, 1]
            if self.labeloutput113.text == "Jaune" : 
                self.labeloutput113.color = [1, 1, 0, 1]

            self.labeloutput114.text = self.spinner4.text
            if self.labeloutput114.text == "Bleu" : 
                self.labeloutput114.color = [0, 0, 1, 1]
            if self.labeloutput114.text == "Vert" : 
                self.labeloutput114.color = [0, 1, 0, 1]
            if self.labeloutput114.text == "Rouge" : 
                self.labeloutput114.color = [1, 0, 0, 1]
            if self.labeloutput114.text == "Jaune" : 
                self.labeloutput114.color = [1, 1, 0, 1]


            #Affichage du nombre de bonnes couleurs bien placées (Ok) 
            
            count14 = 0 
            if self.color[0] == self.spinner1.text : 
                count14 = count14 + 1
            if self.color[1] == self.spinner2.text : 
                count14 = count14 + 1
            if self.color[2] == self.spinner3.text : 
                count14 = count14 + 1
            if self.color[3] == self.spinner4.text : 
                count14 = count14 + 1
            self.labeloutput115.text = str(count14) 

            #Affichage si le joueur à gagné 

            if count14 == 4 : 
                self.pointscore = 3
                self.best()
                self.WinScreen2() 

            #Affichage du nombre de bonnes couleurs (Color)

            count15 = 0 
            elem = 0
            for elem in self.double : 
                if elem in self.double : 
                    if elem in self.spinner1.text : 
                        count15 = count15 + 1
                    elif elem in self.spinner2.text : 
                        count15 = count15 + 1
                    elif elem in self.spinner3.text : 
                        count15 = count15 + 1
                    elif elem in self.spinner4.text : 
                        count15 = count15 + 1
            self.labeloutput116.text = str(count15)

        #Tentative 9 

        elif self.labeloutput111.text != "" and self.labeloutput121.text == "" : 

            #Affichage du nombre de tentatives restantes 

            self.labelTentatives.text = "Tentative restante : 1"

            #Encoder la proposition 
            
            self.labeloutput121.text = self.spinner1.text
            if self.labeloutput121.text == "Bleu" : 
                self.labeloutput121.color = [0, 0, 1, 1]
            if self.labeloutput121.text == "Vert" : 
                self.labeloutput121.color = [0, 1, 0, 1]
            if self.labeloutput121.text == "Rouge" : 
                self.labeloutput121.color = [1, 0, 0, 1]
            if self.labeloutput121.text == "Jaune" : 
                self.labeloutput121.color = [1, 1, 0, 1]
            
            self.labeloutput122.text = self.spinner2.text
            if self.labeloutput122.text == "Bleu" : 
                self.labeloutput122.color = [0, 0, 1, 1]
            if self.labeloutput122.text == "Vert" : 
                self.labeloutput122.color = [0, 1, 0, 1]
            if self.labeloutput122.text == "Rouge" : 
                self.labeloutput122.color = [1, 0, 0, 1]
            if self.labeloutput122.text == "Jaune" : 
                self.labeloutput122.color = [1, 1, 0, 1]

            self.labeloutput123.text = self.spinner3.text
            if self.labeloutput123.text == "Bleu" : 
                self.labeloutput123.color = [0, 0, 1, 1]
            if self.labeloutput123.text == "Vert" : 
                self.labeloutput123.color = [0, 1, 0, 1]
            if self.labeloutput123.text == "Rouge" : 
                self.labeloutput123.color = [1, 0, 0, 1]
            if self.labeloutput123.text == "Jaune" : 
                self.labeloutput123.color = [1, 1, 0, 1]

            self.labeloutput124.text = self.spinner4.text
            if self.labeloutput124.text == "Bleu" : 
                self.labeloutput124.color = [0, 0, 1, 1]
            if self.labeloutput124.text == "Vert" : 
                self.labeloutput124.color = [0, 1, 0, 1]
            if self.labeloutput124.text == "Rouge" : 
                self.labeloutput124.color = [1, 0, 0, 1]
            if self.labeloutput124.text == "Jaune" : 
                self.labeloutput124.color = [1, 1, 0, 1]

            #Affichage du nombre de bonnes couleurs bien placées (Ok) 
            
            count16 = 0 
            if self.color[0] == self.spinner1.text : 
                count16 = count16 + 1
            if self.color[1] == self.spinner2.text : 
                count16 = count16 + 1
            if self.color[2] == self.spinner3.text : 
                count16 = count16 + 1
            if self.color[3] == self.spinner4.text : 
                count16 = count16 + 1
            self.labeloutput125.text = str(count16) 

            #Affichage si le joueur à gagné 

            if count16 == 4 : 
                self.pointscore = 2
                self.best()
                self.WinScreen2() 

            #Affichage du nombre de bonnes couleurs (Color)

            count17 = 0 
            elem = 0
            for elem in self.double : 
                if elem in self.double : 
                    if elem in self.spinner1.text : 
                        count17 = count17 + 1
                    elif elem in self.spinner2.text : 
                        count17 = count17 + 1
                    elif elem in self.spinner3.text : 
                        count17 = count17 + 1
                    elif elem in self.spinner4.text : 
                        count17 = count17 + 1
            self.labeloutput126.text = str(count17)

        #Tentative 10 

        elif self.labeloutput121.text != "" and self.labeloutput131.text == "" : 

            #Affichage du nombre de tentatives restantes 

            self.labelTentatives.text = "Tentative restante : 0"

            #Encoder la proposition 
            
            self.labeloutput131.text = self.spinner1.text
            if self.labeloutput131.text == "Bleu" : 
                self.labeloutput131.color = [0, 0, 1, 1]
            if self.labeloutput131.text == "Vert" : 
                self.labeloutput131.color = [0, 1, 0, 1]
            if self.labeloutput131.text == "Rouge" : 
                self.labeloutput131.color = [1, 0, 0, 1]
            if self.labeloutput131.text == "Jaune" : 
                self.labeloutput131.color = [1, 1, 0, 1]
            
            self.labeloutput132.text = self.spinner2.text
            if self.labeloutput132.text == "Bleu" : 
                self.labeloutput132.color = [0, 0, 1, 1]
            if self.labeloutput132.text == "Vert" : 
                self.labeloutput132.color = [0, 1, 0, 1]
            if self.labeloutput132.text == "Rouge" : 
                self.labeloutput132.color = [1, 0, 0, 1]
            if self.labeloutput132.text == "Jaune" : 
                self.labeloutput132.color = [1, 1, 0, 1]

            self.labeloutput133.text = self.spinner3.text
            if self.labeloutput133.text == "Bleu" : 
                self.labeloutput133.color = [0, 0, 1, 1]
            if self.labeloutput133.text == "Vert" : 
                self.labeloutput133.color = [0, 1, 0, 1]
            if self.labeloutput133.text == "Rouge" : 
                self.labeloutput133.color = [1, 0, 0, 1]
            if self.labeloutput133.text == "Jaune" : 
                self.labeloutput133.color = [1, 1, 0, 1]

            self.labeloutput134.text = self.spinner4.text
            if self.labeloutput134.text == "Bleu" : 
                self.labeloutput134.color = [0, 0, 1, 1]
            if self.labeloutput134.text == "Vert" : 
                self.labeloutput134.color = [0, 1, 0, 1]
            if self.labeloutput134.text == "Rouge" : 
                self.labeloutput134.color = [1, 0, 0, 1]
            if self.labeloutput134.text == "Jaune" : 
                self.labeloutput134.color = [1, 1, 0, 1]


            #Affichage du nombre de bonnes couleurs bien placées (Ok) 
            
            count18 = 0 
            if self.color[0] == self.spinner1.text : 
                count18 = count18 + 1
            if self.color[1] == self.spinner2.text : 
                count18 = count18 + 1
            if self.color[2] == self.spinner3.text : 
                count18 = count18 + 1
            if self.color[3] == self.spinner4.text : 
                count18 = count18 + 1
            self.labeloutput135.text = str(count18) 

            #Affichage si le joueur à gagné 

            if count18 == 4 : 
                self.pointscore = 1
                self.best()
                self.WinScreen2() 
            
            #Affichage si le joueur à perdu 

            else : 
                self.LoseScreen3()

            #Affichage du nombre de bonnes couleurs (Color)

            count19 = 0 
            elem = 0
            for elem in self.double : 
                if elem in self.double : 
                    if elem in self.spinner1.text : 
                        count19 = count19 + 1
                    elif elem in self.spinner2.text : 
                        count19 = count19 + 1
                    elif elem in self.spinner3.text : 
                        count19 = count19 + 1
                    elif elem in self.spinner4.text : 
                        count19 = count19 + 1
            self.labeloutput136.text = str(count19)

    #Fonction si le joueur gagne 

    def WinScreen2(self) : 
        self.__manager.current = "Screen2"

    #Fonction si le joueur perd 

    def LoseScreen3(self) : 
        self.__manager.current = "Screen3"

#Lancement du jeu 

Mastermind().run()