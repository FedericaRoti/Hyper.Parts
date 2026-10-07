# Hyper.Parts, single page: decisioni e stato

Aggiornato: 2026-10-05. Resoconto del lavoro di ricerca e di bozza svolto prima di questa repo.

## Cos'è

Single page informativa di Hyper.Parts, la piattaforma post-vendita ricambi di Due.Zero (Bologna). Oggi Hyper.Parts **non è un SaaS**: l'accesso lo concede il costruttore della macchina, non esiste registrazione autonoma. La pagina presenta un servizio gestito e il testo deve restare coerente con una possibile trasformazione futura in SaaS, senza anticiparla.

`index.html` è una **bozza di direzione**, non la versione finale. Il testo è provvisorio (le frasi portano la classe `.prov`, oggi senza effetto visivo; serve a ritrovarle): quello definitivo lo fornisce l'azienda prima dello sviluppo.

Il brief originale è in [BRIEF.md](BRIEF.md). Alcuni punti sono stati superati dalle decisioni qui sotto; dove c'è conflitto vale questo documento.

## Vincoli

- Un solo file statico, HTML/CSS/JS vanilla, nessun build, nessun backend.
- Niente prezzi pubblici, niente «Prova gratis» o «Registrati», niente login come sezione centrale. Una sola azione: «Parla con noi».
- Solo tema chiaro (una fascia navy di sezione è ammessa). Il tema scuro automatico è stato provato e bocciato: non ha motivazione per un fornitore industriale.
- Il prodotto si mostra solo con immagini e schermate reali, mai ricostruite in HTML o SVG.
- Nessuna texture sul fondo.
- Tono professionale, settore industriale.
- Da evitare i segnali tipici delle pagine generate: etichette e numerazioni decorative, card centrate tutte uguali, trattini lunghi, illustrazioni SVG, icone generiche, `#000` e `#fff` puri.
- Nei testi solo fatti verificati (vedi sotto). Non inventare numeri, clienti, testimonianze, contatti.

## Fatti verificati utilizzabili nei testi

- Tavole ricambi legate alla matricola di ogni macchina.
- QR sulla macchina che apre tavole e documenti dall'app, anche offline.
- Uso da browser e da app (iPhone e Android).
- Listini multivaluta, ricarichi, disponibilità a magazzino.
- Accesso riservato: le credenziali le fornisce il costruttore.
- Due.Zero è a Bologna dal 2008 (non «da oltre vent'anni») e fa documentazione tecnica per l'industria manifatturiera.

Fonti: duezero.eu, scheda App Store, pagina di login di hyperparts.it. La pagina di accesso di hyperparts.it (letta il 2026-10-07) offre: accesso con credenziali, recupero password, pulsante **DEMO**, **Request access** e accesso con **QR dall'app** («Or scan this code with the HyperParts app»). Il testo è in inglese. Tutti questi pulsanti sono azioni interne (`__doPostBack`), non indirizzi: dalla landing si può puntare solo a `https://hyperparts.it/`, non direttamente alla demo né alla richiesta di accesso. `Dashboard.aspx` rimanda al login. La demo non è stata aperta (serve un clic dentro l'app).

## Palette e font

Principio: **struttura in carta, inchiostro e nero (casa Due.Zero); navy e giallo solo dove c'è il prodotto; rosso solo per Due.Zero.** Così il marchio Hyper.Parts resta riconoscibile senza vincolare tutto il resto, e Due.Zero può comparire nel suo colore senza stonare.

| Token | Valore | Uso |
|---|---|---|
| `--bg` | `#EDEDEA` | fondo carta (la stessa di duezero.eu) |
| `--ink` | `#141412` | titoli, testo forte (come duezero.eu) |
| `--text` | `#333333` | testo |
| `--black` | `#0A0A0A` | sezione Due.Zero (come duezero.eu) |
| `--red` | `#E2231A` | solo Due.Zero: pallino del capitolo e freccia del link (il rosso di duezero.eu) |
| `--navy` | `#003B75` | prodotto: vela (taglio), pulsanti, filetti, etichette dei capitoli e di «Con Hyper.Parts» |
| `--accent` | `#FFD300` | prodotto: sfera, `[+]`, pulsante sulla vela |
| `--cut` | `#003B75` (blu, predefinito) oppure `#324646` (grafite) | superficie del taglio |

Il rosso `#CC0000` del login di hyperparts.it non è usato. Font: Big Shoulders Display (titoli), IBM Plex Sans (testo), IBM Plex Mono (etichette e pulsanti).

## Struttura attuale di index.html

1. **Navigazione**: icona reale (stato blu) con nome in stampatello; link alle sezioni; **Accedi** sempre visibile come pulsante a contorno (va a hyperparts.it), anche su mobile.
2. **Apertura**: titolo molto grande su due righe, sottotitolo, pulsante primario «Parla con noi» (nell'angolo sulla vela da 900px in su). Vela blu. Sotto, l'immagine del prodotto parte incorniciata e si allarga a tutta larghezza con lo scroll.
3. **Capitolo 1, Come si vede**: scena fissata su carta, senza vela. Il telefono resta fermo, il testo si sostituisce in tre passi e lo schermo scorre tra tre schermate reali.
4. **Capitolo 2, A chi serve**: su carta, con a sinistra un ritaglio della foto di apertura (il manuale stampato e la linea di confezionamento, che è il «Oggi») e a destra quattro righe: titolo del ruolo, sotto «Oggi» (grigio) e «Con Hyper.Parts» (filetto e etichetta navy). Su mobile l'immagine passa sopra.
5. **Capitolo 3, Come funziona**: su carta. Tre passaggi a sinistra (segno navy, titolo, testo) e a destra un ritaglio della foto di apertura con la dashboard sul portatile.
6. **Capitolo 4, Domande**: quattro domande rapide con risposta visibile (accesso, cosa c'è per ogni macchina, rete, dispositivi), solo con fatti verificati.
7. **Capitolo 5, Due.Zero**: piccola sezione nera, testo chiaro, pallino rosso, link a duezero.eu.
8. **Capitolo 6, Contatti**: due percorsi separati da una riga. «Vuoi attivare Hyper.Parts?» con titolo, frase sull'accesso riservato e l'unica azione primaria «Parla con noi». «Hai già le credenziali?» con tre pulsanti a contorno: Accedi, App iPhone, App Android. Sotto, la vela blu e il footer con solo la riga del copyright.

Il pannello bozza è stato tolto. Le direzioni provate per le sezioni centrali sono in `varianti/`.

## Decisioni prese

- **Modo di comunicare**: affidabilità operativa («il ricambio giusto, al primo ordine»). Scartata la direzione sul valore economico.
- **Carattere dalla coreografia dello scroll e dalla scala tipografica**, non dal colore. Le scene che fissano lo scroll sono ammesse, come su duezero.eu.
- **Scena centrale**: tutto fermo, il testo si sostituisce, lo schermo scorre in verticale.
- **Immagine del prodotto intera** in apertura, che si allarga scorrendo.
- **Pulsanti**: pillola in mono maiuscolo con `[+]`, il linguaggio di duezero.eu.
- **Passaggi tra sezioni**: etichetta «Capitolo N | titolo» con la sfera gialla.
- **La sfera** è il punto di Hyper.Parts e segna solo dove sei (logo, capitoli, avanzamento della scena). Non è un elenco puntato.
- **Il taglio del logo** come elemento riconoscibile: la curva che divide l'icona, in grande, separa la carta da una superficie di colore. Compare in apertura e in chiusura (non nella scena del telefono). Il disco chiaro è la carta, sotto resta `--cut`.
- **Palette per ruoli**: struttura neutra (carta, inchiostro, nero), navy e giallo solo sul prodotto, rosso solo Due.Zero. Titoli in inchiostro, non più in blu.
- **Vela solo in apertura e nel footer**: tolta dalla scena del telefono, perché due curve ravvicinate si pestavano. Colore blu (il livello del logo), non grigio.
- **Due.Zero**: piccola sezione scura prima dei contatti. Nel testo «dal 2008», non «da oltre vent'anni». Niente frase bianca sulla vela nel footer.
- **Sezioni centrali**: «A chi serve» e «Come funziona» su carta, righe allineate, titoli di dimensione media. Meno tipografia: i titoli giganti in maiuscolo sono stati ridotti.
- **Immagini reali nelle sezioni centrali**: per non avere sezioni solo di testo si usano ritagli della foto di apertura (manuale e linea di produzione, dashboard), mai immagini ricostruite. Il footer non ha più la scritta «Bozza, testo provvisorio».
- **Nessuna sottolineatura**: né i segni del testo provvisorio né quelle dei link. I link d'azione sono pulsanti.
- **Azioni con gerarchia**: una sola azione primaria piena («Parla con noi»), le altre a contorno. L'accesso per chi ha già le credenziali è sempre raggiungibile (in alto) e ha un suo percorso in chiusura.

## Scartate, con il motivo

- Bozza «Il conto» con il dato del 20% del fatturato e lo «zero errori» in apertura: il numero sembrava messo a caso, lo zero che cambia colore non aveva senso. Per questo l'hero del brief è superato.
- Fondo scuro o navy a tutta pagina: troppo.
- Bianco e sezioni a colore pieno alternate: sterile il primo, troppo staccate le seconde.
- Pagina a sezioni impilate con immagini e testo: statica, senza carattere.
- Angolo tagliato come passaggio tra sezioni: è la firma di Due.Zero, su Hyper.Parts è forzato.
- Sezione Due.Zero con foto o icone dell'ecosistema: sembrava un inserto estraneo e portava ad altri prodotti. Il blocco nero era stato scartato quando la palette era tutta navy e giallo; con la struttura neutra di carta, inchiostro e nero è tornato, come piccola sezione di testo.
- Sfere usate come decorazione diffusa: sembravano a caso.
- Sfera grande come oggetto protagonista dell'apertura.
- Vetro su tutte le sezioni sopra foto di sfondo: obbliga a riempire il fondo di immagini e diventa prevedibile.
- Tabella di confronto e card: poco convincenti.
- Fascia scura (navy, grafite o nera) per «A chi serve»: nel nero «non ha senso»; il navy pieno era troppo; una sola sezione di colore diverso era solo uno sfondo diverso.
- Fascia gialla a tutta larghezza per «A chi serve»: troppo forte.
- Indice tipografico interattivo (nomi dei ruoli giganti) e ruoli a zig-zag: disordinati, poco chiari, troppa tipografia.
- Frase grande bianca su Due.Zero nel footer, sopra la vela: brutta.
- CTA con sotto tre link sciolti (Accesso clienti, App iPhone, App Android): confusionaria.

## Aperte

- **Colore del taglio**: ora blu `#003B75` (il livello del logo), provato su richiesta. Il grafite `#324646` resta disponibile: si cambia con `data-cut` su `<html>`.
- **Vetro**: provato solo come didascalia sopra l'immagine del prodotto (classe `.glass`), oggi sempre acceso. Da confermare o togliere.
- **Nome**: «Hyper.Parts» o «HyperParts».
- **Destinazione di «Parla con noi»**: oggi `#contatti`, segnaposto.
- **GSAP**: caricato da cdnjs solo per l'immagine che si allarga. duezero.eu non lo usa: va deciso se tenerlo in produzione.
- **Ritmo della parte centrale**: con «A chi serve» e «Come funziona» entrambe su carta e a righe, la parte centrale è calma; il contrasto viene da Due.Zero (nero) e dalla vela. Da rivalutare.
- **Due.Zero**: manca il logo; il rosso `#E2231A` è dedotto dal sito, da confermare come segno di Due.Zero.
- **Testo definitivo**: da ricevere. Il motivo di ogni sezione è in [SEZIONI.md](SEZIONI.md).
- **Spunti da confermare con Due.Zero**: «ciascuno con la propria area» (passo «La crescita») e «video» tra i contenuti; vedi l'elenco in SEZIONI.md.

## Immagini

Le immagini sono in `assets/img/`, scaricate dalle fonti pubbliche dell'azienda. Sono provvisorie: vanno sostituite con gli originali, solo con dati dimostrativi.

| File | Origine | Da chiedere |
|---|---|---|
| `apertura-dashboard-app.webp` (1920×1080) | `duezero.eu/img/eco_hyperparts_bg.webp` | originale; chiarire se è una foto o un fotomontaggio |
| `app-01-home.webp`, `app-02-matricole.webp`, `app-03-scheda-macchina.webp` | schermate della scheda App Store | schermate originali |
| mancante | | schermata desktop della tavola ricambi, eventuale registrazione breve |

In `assets/`:

- `hyperparts-icona-originale.svg`: file ricevuto, contiene sovrapposti lo stato a riposo e quello al passaggio del mouse.
- `hyperparts-icona.svg`: solo lo stato a riposo, ricavato dall'originale.
- `hyperparts-icona-hover.svg`: solo lo stato al passaggio del mouse.

Il logo è l'icona. In pagina il nome è composto in testo, con la sfera al posto del punto.

## Note tecniche

- Gli stati iniziali delle animazioni si applicano solo sotto `html.js:not(.reduce)`: senza JavaScript o con movimento ridotto la pagina è già nello stato finale.
- Nessun listener di `scroll`: si usano `IntersectionObserver` e `position: sticky`. La scena cambia passo con tre sentinelle e `rootMargin: '-49% 0px -49% 0px'`.
- `IntersectionObserver` non rileva un elemento ritagliato del tutto da `clip-path`: si osserva il contenitore.
- Il taglio è un cerchio di 400vw color carta dentro un contenitore `.cut-host` con `overflow: hidden` e fondo `--cut`.
- Sotto i 900px il pulsante dell'apertura resta accanto al testo; sopra, passa nell'angolo sul taglio.

## Non verificato

Fluidità del movimento su un browser vero, tocco su telefono reale, Safari e Firefox, `prefers-reduced-motion`. Controllati solo a schermo, a 1024px e 375px, in un browser basato su Chromium: struttura, passi della scena, assenza di scorrimento orizzontale e di errori in console.
