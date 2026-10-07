# La demo di hyperparts.it: come è fatta e cosa serve per sistemarla

Ricavato dal codice delle pagine che il browser scarica (letto il 2026-10-07, solo lettura). Il codice del server e il database non si vedono da fuori: dove è un'ipotesi è scritto.

## Com'è costruita
- **È l'app vera, non un sito a parte.** Il pulsante DEMO fa entrare come utente `demo@demo.it`, «Bruce Wayne (2.0)», del cliente fittizio `WAYNE-CORP`. Stesso indirizzo e stesse pagine di chi usa l'app con credenziali. (Ipotesi: stessi server e stessa base dati, con un cliente di prova dentro.)
- **Tecnologia**: ASP.NET su IIS (pagine `.aspx`), jQuery e Bootstrap, tabelle DataTables, `svg-pan-zoom` per zoom e spostamenti, `pdf.js` per i documenti. I dati arrivano da chiamate interne alle pagine (per esempio `Dettaglio-Matricola.aspx/ElencoGruppi`).
- **Immagini e file** sono su un archivio cloud, in cartelle per cliente e codice dell'unità (per esempio `hyperparts-gruppi/WAYNE-CORP/92252S0025/92252S0025.jpg`).
- **Pagine principali**: Dashboard, Products (`Parco-macchine`), Plants (`Linee`), carrello (preventivi), scheda macchina (`Dettaglio-Matricola`), Warehouse (`magazzino`), Recommended (`ricambiconsigliati`), richiesta di supporto.

## La scheda macchina, passo per passo
1. La pagina contiene il **disegno della macchina come immagine vettoriale (SVG)**, con zoom.
2. Ogni forma del disegno (poligoni, cerchi, rettangoli, testi) viene resa **cliccabile da uno script**, con una regola unica per tutte.
3. Un clic porta a `ConvertiGruppoMatricolaTavola0.aspx?CODICEGRUPPO=<id della forma>`: l'app cerca l'**unità** (gruppo) con quel codice e mostra la sua **tavola** con i ricambi.
4. Se il codice non corrisponde a un'unità collegata a quella matricola, compare «**Unit not available in your machine:**» e un riquadro vuoto.

## Perché si blocca (la causa, secondo il codice)
Nel disegno della macchina SN00002 c'è **una sola zona collegata a un'unità**: «USCITA PRODOTTO (CON SALDATURA)», codice `92252S0025`. Ma tutte le altre forme sono cliccabili uguale. Cliccare un componente qualsiasi porta quindi a un'unità che non esiste per quella macchina, ed è quello che hai visto. Non è un tuo errore e non è un guasto: sono dati e collegamenti mancanti, più una regola che rende cliccabile tutto.

## Cosa serve per sistemarla, con dati fittizi
**Contenuti (il lavoro più lungo, lo fa Due.Zero)**
- Per ogni macchina della demo, **6–10 unità** inventate: codice, nome, immagine della tavola, elenco dei ricambi (codice, descrizione, quantità). Codici di fantasia, non quelli di clienti veri. Nessun prezzo reale.
- Per ognuna, la **zona cliccabile** nel disegno collegata al suo codice.
- **Warehouse**: righe di magazzino di esempio per quei ricambi (quantità, tempi di consegna).
- **Recommended**: 5–10 ricambi consigliati.
- **Documentazione**: 2–3 documenti di prova (per esempio un manuale finto in PDF).
- **Multimedia**: un breve video generico.
- **Plants**: almeno una linea con le due macchine.

**Codice (interventi piccoli)**
- Rendere cliccabili **solo** le forme che hanno un'unità collegata.
- Sostituire il messaggio di errore con uno completo, per esempio «Questa zona non ha una tavola: scegli un'area evidenziata.»
- Per l'utente demo: nascondere o disattivare ciò che scrive davvero («Nuova macchina», caricamento e cancellazione di documenti, invio delle richieste di supporto, invio dei preventivi).
- Nascondere le linguette che in demo restano vuote.
- Una sola lingua nell'interfaccia e un solo nome del prodotto.
- Un **azzeramento automatico** dei dati della demo, per esempio ogni notte.
- Un **indirizzo diretto** che avvia la demo (adesso è un pulsante interno): senza, dalla landing non si arriva alla demo.

## E per metterla dentro il sito
- «Dentro il sito» vuol dire mostrare l'app vera dentro la pagina (finestra incorporata) o aprirla in una scheda. Con una finestra incorporata servono: l'indirizzo diretto di sopra, il permesso dell'app a comparire in un'altra pagina e, se la landing è su un dominio diverso, un cambio di impostazione dei cookie (oggi la sessione ha `SameSite=Lax` e in una finestra incorporata su un altro dominio non verrebbe inviata).
- L'app è pensata per il computer: va provata da telefono prima di incorporarla.
- Ordine consigliato: prima sistemare la demo, poi l'indirizzo diretto con un pulsante «Guarda la demo» nella landing, e solo dopo, se serve, incorporarla.
