# Hyper.Parts, single page: decisioni e stato

Aggiornato: 2026-10-02. Resoconto del lavoro di ricerca e di bozza svolto prima di questa repo.

## Cos'è

Single page informativa di Hyper.Parts, la piattaforma post-vendita ricambi di Due.Zero (Bologna). Oggi Hyper.Parts **non è un SaaS**: l'accesso lo concede il costruttore della macchina, non esiste registrazione autonoma. La pagina presenta un servizio gestito e il testo deve restare coerente con una possibile trasformazione futura in SaaS, senza anticiparla.

`index.html` è una **bozza di direzione**, non la versione finale. Il testo è provvisorio (in pagina è sottolineato a tratteggio, classe `.prov`): quello definitivo lo fornisce l'azienda prima dello sviluppo.

Il brief originale è in [BRIEF.md](BRIEF.md). Alcuni punti sono stati superati dalle decisioni qui sotto; dove c'è conflitto vale questo documento.

## Vincoli

- Un solo file statico, HTML/CSS/JS vanilla, nessun build, nessun backend.
- Niente prezzi pubblici, niente «Prova gratis» o «Registrati», niente login come sezione centrale. Una sola azione: «Parla con noi».
- Solo tema chiaro. Il tema scuro automatico è stato provato e bocciato: non ha motivazione per un fornitore industriale.
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
- Due.Zero è a Bologna da oltre vent'anni e fa documentazione tecnica per l'industria manifatturiera.

Fonti: duezero.eu, scheda App Store, pagina di login di hyperparts.it. L'ambiente demo di hyperparts.it non è stato aperto.

## Palette e font

Dal logo dell'app, non dal sito corporate.

| Token | Valore | Uso |
|---|---|---|
| `--navy` | `#003B75` | titoli, pulsante |
| `--accent` | `#FFD300` | solo sfera, `[+]` e pulsante sul taglio |
| `--cut` | `#324646` (grafite) oppure `#003B75` | superficie del taglio |
| `--ink` | `#1F2426` | titolo d'apertura, testo forte |
| `--text` | `#333333` | testo |
| `--bg` | `#EDEDEA` | fondo carta, preso da duezero.eu |

Il rosso `#CC0000` del brief non è usato. Font: Big Shoulders Display (titoli), IBM Plex Sans (testo), IBM Plex Mono (etichette e pulsanti).

## Struttura attuale di index.html

1. **Apertura**: titolo molto grande su due righe, sottotitolo, pulsante. Sotto, l'immagine del prodotto parte incorniciata e si allarga a tutta larghezza con lo scroll.
2. **Capitolo 1, Come si vede**: scena fissata. Il telefono resta fermo, il testo si sostituisce in tre passi (inquadra il QR, apre la matricola, trova quello che serve) e lo schermo scorre tra tre schermate reali.
3. **Capitolo 2, A chi serve**: quattro righe, una per ruolo. In ogni riga «Oggi» lascia il posto a «Con Hyper.Parts» quando la riga supera la metà dello schermo.
4. **Capitolo 3, Come funziona**: tre passaggi (la richiesta, il catalogo costruito insieme, la crescita).
5. **Capitolo 4, Due.Zero**: due righe sull'azienda e il link.
6. **Capitolo 5, Contatti**: titolo grande, pulsante, link ad accesso clienti e alle app.

Il pannello scuro in basso a sinistra è uno strumento di bozza (segni del testo provvisorio, colore del taglio, vetro) e va tolto dalla versione finale.

## Decisioni prese

- **Modo di comunicare**: affidabilità operativa («il ricambio giusto, al primo ordine»). Scartata la direzione sul valore economico.
- **Carattere dalla coreografia dello scroll e dalla scala tipografica**, non dal colore. Le scene che fissano lo scroll sono ammesse, come su duezero.eu.
- **Scena centrale**: tutto fermo, il testo si sostituisce, lo schermo scorre in verticale.
- **Immagine del prodotto intera** in apertura, che si allarga scorrendo.
- **Pulsanti**: pillola in mono maiuscolo con `[+]`, il linguaggio di duezero.eu.
- **Passaggi tra sezioni**: etichetta «Capitolo N | titolo» con la sfera gialla.
- **La sfera** è il punto di Hyper.Parts e segna solo dove sei (logo, capitoli, avanzamento della scena). Non è un elenco puntato.
- **Il taglio del logo** come elemento riconoscibile: la curva che divide l'icona, in grande, separa la carta da una superficie di colore. Compare in apertura, nella scena e in chiusura. Il disco chiaro è la carta, sotto resta `--cut`.
- **Palette non ovunque**: fondo carta, blu sui titoli, giallo su pochi dettagli.
- **Sezione Due.Zero**: solo due righe sull'azienda.

## Scartate, con il motivo

- Bozza «Il conto» con il dato del 20% del fatturato e lo «zero errori» in apertura: il numero sembrava messo a caso, lo zero che cambia colore non aveva senso. Per questo l'hero del brief è superato.
- Fondo scuro o navy a tutta pagina: troppo.
- Bianco e sezioni a colore pieno alternate: sterile il primo, troppo staccate le seconde.
- Pagina a sezioni impilate con immagini e testo: statica, senza carattere.
- Angolo tagliato come passaggio tra sezioni: è la firma di Due.Zero, su Hyper.Parts è forzato.
- Sezione Due.Zero con blocco nero, foto o icone dell'ecosistema: sembrava un inserto estraneo e portava ad altri prodotti.
- Sfere usate come decorazione diffusa: sembravano a caso.
- Sfera grande come oggetto protagonista dell'apertura.
- Vetro su tutte le sezioni sopra foto di sfondo: obbliga a riempire il fondo di immagini e diventa prevedibile.
- Tabella di confronto e card: poco convincenti.

## Aperte

- **Colore del taglio**: grafite `#324646` o blu `#003B75`. Entrambi vengono dall'icona: a riposo la metà sotto la curva è grigio scuro, al passaggio del mouse diventa blu. In pagina si cambia con `data-cut="blu"` su `<html>`.
- **Vetro**: provato solo come didascalia sopra l'immagine del prodotto (classe `.glass`, si spegne con `.no-glass` su `<html>`). Da confermare o togliere.
- **Nome**: «Hyper.Parts» o «HyperParts».
- **Destinazione di «Parla con noi»**: oggi `#contatti`, segnaposto.
- **GSAP**: caricato da cdnjs solo per l'immagine che si allarga. duezero.eu non lo usa: va deciso se tenerlo in produzione.
- **Sezioni da rifinire**: la struttura è approvata, alcune sezioni sono ancora da lavorare.
- **Testo definitivo**: da ricevere.

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
