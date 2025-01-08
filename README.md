LEGGERE E SEGUIRE LE ISTRUZIONI PER GIOCARE

## Descrizione
Il progetto Quiz consente agli utenti di rispondere a domande multiple con 4 opzioni di risposta, Ogni domanda ha una sola risposta corretta, L'utente deve selezionare la risposta corretta per procedere alla domanda successiva. 

# Quiz Game sul Terminale

Benvenuto! Questo è il mio **quiz game** eseguibile direttamente sul terminale.

## Come Usarlo

1. **Copiare il repository**:
   - Utilizzare il protocollo HTTPS per clonare il repository sul proprio dispositivo.

2. **Preparazione dell'ambiente**:
   - Assicurarsi che il file Python e il file JSON si trovino nella stessa directory, senza una cartella statica.
   - Creare un ambiente virtuale:
     ```bash
     python -m venv venv
     source venv/bin/activate  # Su Windows: venv\Scripts\activate
     ```
   - Installare le librerie richieste tramite `pip`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Eseguire il progetto**:
   - Nel terminale, digitare:
     ```bash
     python progetto.py
     ```
   - Il file verrà eseguito. 

4. **Documentazione visuale**:
   - Il progetto include un diagramma generato con **PlantUML** che spiega il funzionamento tramite una mappa.
   
## Funzionamento
## Menù Principale

Il progetto presenta un menù principale con le seguenti opzioni:

1. **Inizia Quiz**: 
   - Avvia il quiz e consente di rispondere a varie domande sulle classi e sulla programmazione orientata agli oggetti (OOP) in Python.
   - Al termine, verrà mostrato il punteggio finale. 

2. **Aggiungi Domanda**:
   - Permette di aggiungere nuove domande al quiz. 
   - È possibile inserire:
     - La domanda.
     - La risposta corretta.
     - Il punteggio associato alla domanda.
   - La domanda viene automaticamente salvata nel file JSON, rendendola disponibile per futuri utilizzi.

3. **Esci**:
   - Termina il programma ringraziando l'utente per aver giocato.

## Buon Divertimento!

Inizia subito il quiz e metti alla prova le tue conoscenze su Python e OOP!

![image](https://github.com/user-attachments/assets/6005a18c-0c5b-4778-b080-4adf65ecfbb6)


## Esempio di domanda
Ecco un esempio di formato delle domande nel file JSON:

![image](https://github.com/user-attachments/assets/40bd49f1-028e-4146-a8df-9b618db59c11)

In questo esempio, la risposta corretta è la terza opzione (indice 2).

## Autori
- [Simon Kola]
## Licenza
Questo progetto è distribuito sotto la licenza MIT. Consulta il file LICENSE per ulteriori dettagli.
