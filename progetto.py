from dataclasses import dataclass
import json
from typing import List
import colorama
from colorama import Fore, Style
import time
import os

@dataclass
class Domanda:
    testo: str
    opzioni: List[str]
    risposta_corretta: int
    punti: int = 1

class Quiz:
    def __init__(self, file_quiz: str):
        self.file_quiz = file_quiz
        self.domande = []
        self.punteggio = 0
        colorama.init()
        self.carica_domande()

    def carica_domande(self):
        with open(self.file_quiz, 'r', encoding='utf-8') as f:
            dati = json.load(f)
            for d in dati:
                domanda = Domanda(
                    testo=d['testo'],
                    opzioni=d['opzioni'],
                    risposta_corretta=d['risposta_corretta'],
                    punti=d.get('punti', 1)
                )
                self.domande.append(domanda)

    def salva_domande(self):
        with open(self.file_quiz, 'w', encoding='utf-8') as f:
            dati = []
            for d in self.domande:
                dati_domanda = {
                    'testo': d.testo,
                    'opzioni': d.opzioni,
                    'risposta_corretta': d.risposta_corretta,
                    'punti': d.punti
                }
                dati.append(dati_domanda)
            json.dump(dati, f, indent=4, ensure_ascii=False)

    def aggiungi_domanda(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.CYAN}Aggiungi una nuova domanda{Style.RESET_ALL}")
        testo = input("Inserisci il testo della domanda:")
        opzioni = []
        for i in range(4):
            opzione = input(f"Inserisci l'opzione {i+1}:")
            opzioni.append(opzione)
        while True:
            try:
                risposta_corretta = int(input("Numero dell'opzione corretta (1-4):")) 
                if 1 <= risposta_corretta <= 4:
                    break
                print("Inserisci un numero tra 1 e 4")
            except ValueError:
                print("Inserisci un numero valido")
        punti = int(input("Punti per questa domanda:"))
        self.domande.append(Domanda(testo, opzioni, risposta_corretta, punti))
        self.salva_domande()

    def mostra_domanda(self, domanda: Domanda):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{Fore.CYAN}{domanda.testo}{Style.RESET_ALL}")
        for i, opzione in enumerate(domanda.opzioni, 1):
            print(f"{i}. {opzione}")

    def gioca(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.GREEN}Benvenuto al Quiz su Python, vediamo quante ne sai ;){Style.RESET_ALL}")
        input("Premi INVIO per iniziare il quiz")
        for domanda in self.domande:
            self.mostra_domanda(domanda)
            while True:
                try:
                    risposta = int(input("Scegli la risposta (1-4):").strip()) 
                    if 1 <= risposta <= 4:
                        break
                    print("inserisci un numero tra 1 e 4")
                except ValueError:
                    print("inserisci un numero valido")
            
            if risposta == domanda.risposta_corretta:
                print(f"{Fore.GREEN}corretto! +{domanda.punti} punti{Style.RESET_ALL}")
                self.punteggio += domanda.punti
            else:
                print(f"{Fore.RED}sbagliato! la risposta corretta era {domanda.risposta_corretta}{Style.RESET_ALL}")
            time.sleep(2)
        
        print(f"\n{Fore.YELLOW}quiz completato! punteggio finale: {self.punteggio}{Style.RESET_ALL}")
        input("Premi INVIO per continuare")

    def menu_principale(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Fore.CYAN}Menu Principale{Style.RESET_ALL}")
            print("1. Inizia il quiz")
            print("2. Aggiungi una domanda")
            print("3. Esci")
            
            scelta = input("Scegli un'opzione:").strip()
            if scelta == '1':
                self.gioca()
            elif scelta == '2':
                self.aggiungi_domanda()
            elif scelta == '3':
                print("grazie per aver giocato!")
                break
            else:
                print("scelta non valida")
                time.sleep(1)

if __name__ == "__main__":
    quiz = Quiz("domande.json")
    quiz.menu_principale()