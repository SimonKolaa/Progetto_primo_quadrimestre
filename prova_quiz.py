from dataclasses import dataclass
import json
from typing import List
import colorama
from colorama import Fore, Style
import time

@dataclass
class Domanda:
    testo: str
    opzioni: List[str]
    risposta_corretta: int
    punti: int = 2  # Ogni domanda giusta vale 2 punti

class Quiz:
    def __init__(self, file_quiz: str = 'static/prova_quiz.json'):
        self.file_quiz = file_quiz
        self.domande = []
        self.punteggio = 0
        self.carica_domande()
        colorama.init()

    def carica_domande(self):
        with open(self.file_quiz, 'r') as f:
            dati = json.load(f)
            self.domande = []
            for i in dati:
                domanda = Domanda(
                    testo=i['text'],
                    opzioni=i['options'],
                    risposta_corretta=i['correct_answer'],
                    punti=i['points']
                )
                self.domande.append(domanda)

    def salva_domande(self):
        with open(self.file_quiz, 'w') as f:
            dati = []
            for i in self.domande:
                dati_domanda = {
                    'text': i.testo,
                    'options': i.opzioni,
                    'correct_answer': i.risposta_corretta,
                    'points': i.punti
                }
                dati.append(dati_domanda)
            json.dump(dati, f, indent=4)

    def aggiungi_domanda(self):
        testo = input("inserisci il testo della domanda:")
        opzioni = []
        for i in range(4):
            opzione = input(f"inserisci l'opzione {i+1}: ")
            opzioni.append(opzione)
        risposta_corretta = int(input("numero dell'opzione corretta (1-4): ")) - 1
        punti = int(input("punti per questa domanda: "))
        nuova_domanda = Domanda(testo, opzioni, risposta_corretta, punti)
        self.domande.append(nuova_domanda)
        self.salva_domande()

    def mostra_domanda(self, domanda: Domanda):
        print(Fore.YELLOW + domanda.testo + Style.RESET_ALL)
        for i, opzione in enumerate(domanda.opzioni):
            print(f"{i + 1}. {opzione}")

    def verifica_risposta(self, domanda: Domanda):
        risposta = int(input("inserisci il numero della risposta corretta: ")) - 1
        if risposta == domanda.risposta_corretta:
            print(Fore.GREEN + "risposta corretta!" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "risposta sbagliata" + Style.RESET_ALL)
            return False

    def run(self):
        print("benvenuto al quiz su Python! Scrivi 'gioca' per iniziare")
        comando = input("scrivi 'gioca' per iniziare: ").strip().lower() #ai
        if comando == 'gioca':
            while self.punteggio < 10:
                for domanda in self.domande:
                    self.mostra_domanda(domanda)
                    if self.verifica_risposta(domanda):
                        self.punteggio += domanda.punti
                        print(f"punteggio attuale: {self.punteggio}")
                        if self.punteggio >= 10:
                            print("Hai vinto!")
                    else:
                        self.punteggio = 0
                        print("Risposta sbagliata. Punteggio resettato a 0.")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run()