# Demo di hyperparts.it: cosa si vede da fuori

Letta il 2026-10-07, in sola lettura (nessun ordine, nessuna modifica). Solo il codice delle pagine, non il JavaScript in esecuzione: grafici, mappa e dati caricati dopo non sono stati visti.

## Come si entra
- Dalla pagina `https://hyperparts.it/` il pulsante **DEMO** è un'azione dell'app (`__doPostBack`), non un indirizzo. Non serve nessuna credenziale.
- La demo si apre come utente di prova «Bruce Wayne (2.0)».
- Quindi dalla landing non esiste un link diretto alla demo: si può puntare solo alla pagina di accesso. Un link diretto richiede una modifica all'app (un indirizzo che avvia la demo).

## Cosa contiene
- **Dashboard** (grafici e mappa caricati dopo: non verificati).
- **Products** (`Parco-macchine.aspx`): due macchine, HYPER-MACHINE (SN00002, «Avvolgitrice automatica») e HYPER-ROBOT (SN00001, «Montatore automatico»), con un pulsante «Nuova macchina».
- **Plants** (`Linee.aspx`): la pagina «Your plants» risulta **vuota** nel codice; da controllare se è voluto o se i dati arrivano dopo.
- **Carrello** (`carrello`): preventivo RFQ00134, «Quotations not sent», 2 articoli.
- **Richiesta di supporto**: modulo con nome, email, destinatario, oggetto, descrizione, fino a 3 allegati da 10 MB e «Cattura schermata».
- Accesso con QR dall'app nella pagina di login. Piè di pagina «Credits: Due.Zero» e link agli store dell'app.

## Incoerenze che si vedono (non sono per forza errori)
- **Lingua mista**: interfaccia in inglese («Your products», «Basket», «Menu») con parti in italiano («Richiesta di Supporto», «Il mio profilo», «Trascina i file qui», nomi delle macchine).
- **Nome del prodotto**: «Hyperparts» nel titolo delle pagine, «HyperParts» nel piè di pagina e nel logo. È lo stesso punto aperto del sito.
- **Pagina Plants vuota** (vedi sopra).

## Da chiedere a chi sviluppa l'app
- Un indirizzo che avvii la demo senza passare dal login.
- Se la demo si azzera e se più visitatori condividono lo stesso utente di prova.
- Se in demo si possono creare macchine o inviare preventivi e richieste di supporto veri (il pulsante «Nuova macchina» e il modulo supporto sono attivi).

## Cosa non funziona (segnalato da chi l'ha provata, 2026-10-07)
Percorso: Products → HYPER-MACHINE (SN00002) → scheda della macchina → clic su un componente del disegno.
1. La scheda della macchina si apre bene: disegno esploso, con il suggerimento «Passa con il mouse sul tuo prodotto.. / Clicca e visualizza il gruppo! Enjoy :-)» (in italiano, mentre il resto è in inglese).
2. Cliccando un componente compare «**Unit not available in your machine:**» con il solo pulsante BACK, sopra un riquadro grigio vuoto. Il messaggio finisce con i due punti e non dice quale unità manca. Probabilmente l'unità cliccata non è collegata a questa matricola nei dati della demo.
3. Il pannello **Warehouse** (linguetta a sinistra) non si apre. Non è verificato se sia un errore dell'app o dati demo mancanti.
4. Anche **Plants** è vuota (vedi sopra).

## Proposta per chi sviluppa l'app: una demo senza vicoli ciechi
Una demo serve a convincere, quindi ogni clic deve portare a qualcosa. Una lista di controllo prima di renderla pubblica:
- Ogni componente cliccabile del disegno porta a un'unità che esiste per quella matricola (e ogni unità ha ricambi).
- Warehouse e Plants hanno dati di esempio; le linguette che non servono in demo si nascondono.
- I messaggi di errore sono completi e dicono cosa fare («Questa unità non è disponibile per la tua macchina: scegli un altro componente»).
- Una lingua sola nell'interfaccia (o una scelta chiara) e un solo nome: «HyperParts» o «Hyperparts».
- I dati della demo si azzerano e le azioni che scrivono (nuova macchina, preventivo, richiesta di supporto) non arrivano a nessuno.
- Una prova completa da telefono e da computer prima di collegare la demo dalla landing.
