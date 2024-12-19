# Progetto Quiz

## Descrizione
Il progetto Quiz è un'applicazione interattiva che consente agli utenti di rispondere a domande multiple con 4 opzioni di risposta. Ogni domanda ha una sola risposta corretta. L'utente deve selezionare la risposta corretta per procedere alla domanda successiva. 

Questo progetto utilizza un file JSON per memorizzare le domande e le risposte e un file Python per gestire la logica del gioco e l'interfaccia utente.

## Installazione
Segui questi passaggi per configurare l'ambiente di sviluppo e avviare il progetto:

```bash
# Crea un ambiente virtuale
python -m venv venv

# Attiva l'ambiente virtuale
# Su Linux/macOS:
source venv/bin/activate
# Su Windows:
venv\Scripts\activate

# Installa le dipendenze
pip install -r requirements.txt
```

## Utilizzo
Dopo aver configurato l'ambiente, esegui il file principale per iniziare il quiz:

```bash
python src/quiz.py
```

Assicurati che il file JSON contenente le domande sia presente nella directory indicata dallo script Python.

## Esempio di domanda
Ecco un esempio di formato delle domande nel file JSON:

[
  {
    "domanda": "Cosa sono le classi in Python?",
    "opzioni": [
      "Strutture che permettono di gestire cicli e condizioni.",
      "Funzioni speciali che servono solo a calcolare valori numerici.",
      "Modelli o schemi per creare oggetti, definendo attributi e metodi.",
      "Librerie predefinite utilizzate per importare funzionalità extra."
    ],
    "corretta": 2
  }
]
```

In questo esempio, la risposta corretta è la terza opzione (indice 2).

## Autori
- [Simon Kola]
## Licenza
Questo progetto è distribuito sotto la licenza MIT. Consulta il file LICENSE per ulteriori dettagli.
