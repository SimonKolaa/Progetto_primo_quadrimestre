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
    punti: int = 1

class Quiz:
    def __init__(self, file_quiz: str):
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
        testo = input("Inserisci il testo della domanda: ")
        opzioni = []
        for i in range(4):
            opzione = input(f"Inserisci l'opzione {i+1}: ")
            opzioni.append(opzione)
        risposta_corretta = int(input("Numero dell'opzione corretta (1-4): ")) - 1
        punti = int(input("Punti per questa domanda: "))
        nuova_domanda = Domanda(testo, opzioni, risposta_corretta, punti)
        self.domande.append(nuova_domanda)
        self.salva_domande()

    def mostra_domanda(self, domanda: Domanda):
        print(Fore.YELLOW + domanda.testo + Style.RESET_ALL)
        for i, opzione in enumerate(domanda.opzioni):
            if i == domanda.risposta_corretta:
                print(Fore.GREEN + f"{i + 1}. {opzione} (corretta)" + Style.RESET_ALL)
            else:
                print(f"{i + 1}. {opzione}")

    def verifica_risposta(self, domanda: Domanda):
        risposta = int(input("Inserisci il numero della risposta corretta: ")) - 1
        if risposta == domanda.risposta_corretta:
            print(Fore.GREEN + "Risposta corretta!" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "Risposta sbagliata." + Style.RESET_ALL)
            return False

    def esegui(self):
        while True:
            print("1. Inizia il quiz")
            print("2. Aggiungi una domanda")
            print("3. Esci")
            scelta = input("Scegli un'opzione: ")
            if scelta == '1':
                for i in self.domande:
                    self.mostra_domanda(i)
                    if self.verifica_risposta(i):
                        self.punteggio += i.punti
                print(f"Il tuo punteggio finale è: {self.punteggio}")
                break
            elif scelta == '2':
                self.aggiungi_domanda()
            elif scelta == '3':
                break
            else:
                print("Scelta non valida, Riprova")
