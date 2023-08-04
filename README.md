![](https://img.shields.io/badge/Python-3.8%2B-green.svg)
![](https://img.shields.io/badge/Standard-DublinCore-violet.svg)
![](https://img.shields.io/badge/Export-CSV-orange.svg)

<p align="center">
  <img src="https://github.com/logo94/catabot/blob/main/img/logo.png" />
</p>

Catabot è un'applicazione Desktop scritta in linguaggio Python che permette l'estrazione automatica di metadati descrittivi da pagine web.

Come standard di metadatazione Catabot utilizza come riferimento l'insieme dei 15 elementi descrittivi elaborati dal Web Archiving Metadata Working Group (WAM) di OCLC, espressi secondo lo standard Dublin Core e trasversali rispetto ai principali standard di metadatazione (Dublin Core, MARC21, EAD, MODS e Schema.org).

Partendo da un URL o da una lista di link, per la raccolta dei metadati Catabot interroga direttamente le pagine di un sito e attraverso web scraping estrae informazioni strutturate che verranno esportate in formato CSV.

Per l'ottenimento dei link da utilizzare come punto di partenza per la raccolta dei metadati sono attualmente disponibili tre modalità:
* Interrogazione OAI Endpoint
* Scraping dei link di un sito o di una sua porzione partendo da un singolo URL o da un URL progressivo
* Interrogazione Archive-it API Endpoint (necessario un Archive-it API Token)
* Interrogazione RSS Feed (non ancora disponibile)

Per l'ottenimento dei metadati descrittivi le funzionalità attualmente supportate sono:
* Interrogazione OAI Endpoint
* Scraping dei metatags per la SEO
* Scraping di elementi HTML

Le implementazioni future potranno comprendere:
* Scraping di metatags o elementi HTML da file WARC
* Export in formato JSON
* Opzioni user-friendly per il download dell'applicazione

Per maggiori informazioni consulta la sezione [Wiki](https://github.com/logo94/catabot/wiki)

## Requisiti ##
Per l'utilizzo degli scripts è necessario aver scaricato `Python 3.8+` sul proprio dispositivo, per installare Python seguire le istruzioni riportate al seguente [link](https://www.python.org/downloads/).

Una volta eseguito il download è possibile verificare le versioni di `Python` e `pip` tramite i comandi:

```
python --version
```
```
pip --version
```

## Installazione ##
Per scaricare l'applicazione localmente premere il tasto verde 'Code' in alto a destra e scegliere il sistema di download preferito, nel caso non si conoscano le opzioni elencate, premere sul tasto 'Download ZIP':

<p align="center">
  <img src="https://github.com/logo94/catabot/blob/main/img/catabot-download.png" />
</p>

Una volta scaricato il file, decomprimerlo ed entrare nella cartella risultante

## Ambiente virtuale ##
Per non compromettere l'installazione di Python e le relative librerie è consigliabile creare un ambiente virtuale; per la sua creazione, una volta dentro la cartella dell'applicazione, procedere come segue:

Aprire il terminale all'interno della cartella (premere il tasto destro del mouse all'interno di uno spazio vuoto della cartella e selezionare l'opzione Apri nel Terminale)

Creare l'ambiente virtuale, quindi digitare:
```
python -m venv pyenv
```
oppure, in caso di errore:
```
python3 -m venv pyenv
```

### Linux
Per attivare l'ambiente virtuale con un sistema operativo Linux digitare:
```
source pyenv/bin/activate
```
### Windows
L'attivazione dell'ambiente virtuale su sistema operativo Windows richiede i privilegi di Amministratore di sistema, è quindi necessario aprire il Terminale o Windows PowerShell come amministratore. Una volta eseguita la procedura sopra riportata digitare:
```
pyenv\Scripts\activate
```

>Nel caso in cui non ci sia la possibilità di ottenere i privilegi di amministratore questo passaggio può essere saltato in modo che sia utilizzato l'ambiente virtuale Python di sistema.

## Librerie ##
Per il suo funzionamento Catabot utilizza una serie di librerie esterne, per il corretto funzionamento dell'applicazione è necessario procedere con il download di tutti i pacchetti necessari, ovvero:

```
pip install -r requirements.txt
```
### Windows
Per l'installazione delle librerie è necessario disporre dei perivilegi di amministratore di sistema, in alternativa è possibile avviare l'installazione senza privilegi specifici attraverso il comando:
```
pip install -r requirements.txt --user
```
> Eventuali messaggi di Warning durante l'installazione potranno essere ignorati



## Utilizzo ##
Una volta scaricato il repository e scaricate le librerie necessarie, per avviare l'applicazione sarà sufficiente eseguire il comando:
```
python catabot.py
```
oppure:
```
python3 catabot.py
```
Si aprirà la seguente finestra:

<p align="center">
  <img src="https://github.com/logo94/catabot/blob/main/img/screen.png" />
</p>

L'applicazione si aprirà e sarà pronta per essere utilizzata, per maggiori dettagli consulta la sezione [Wiki](https://github.com/logo94/catabot/wiki)

Per i successivi utilizzi sarà sufficiente entrare all'interno della cartella dell'applicazione, aprire il Terminale, attivare l'ambiente virtuale nel caso questo sia stato creato e avviare l'applicazione:
```
python catabot.py
```
