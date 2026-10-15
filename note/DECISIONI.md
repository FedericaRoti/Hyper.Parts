# Hyper.Parts, single page: decisioni e stato

Aggiornato: 2026-10-05. Resoconto del lavoro di ricerca e di bozza svolto prima di questa repo.

## Cos'è

Single page informativa di Hyper.Parts, la piattaforma post-vendita ricambi di Due.Zero (Bologna). Oggi Hyper.Parts **non è un SaaS**: l'accesso lo concede il costruttore della macchina, oppure si chiede con il modulo «Richiedi accesso» della pagina di accesso (email, telefono e password: l'account viene attivato dopo la richiesta, non subito). La pagina presenta un servizio gestito e il testo deve restare coerente con una possibile trasformazione futura in SaaS, senza anticiparla.

`docs/index.html` è una **bozza di direzione**, non la versione finale. Il testo è provvisorio (le frasi portano la classe `.prov`, oggi senza effetto visivo; serve a ritrovarle): quello definitivo lo fornisce l'azienda prima dello sviluppo.

Il brief originale è in [BRIEF.md](BRIEF.md). Alcuni punti sono stati superati dalle decisioni qui sotto; dove c'è conflitto vale questo documento.

## Vincoli

- Un solo file statico, HTML/CSS/JS vanilla, nessun build, nessun backend.
- Niente prezzi pubblici, niente «Prova gratis» o «Registrati». Dal 2026-10-14 l'accesso (login) è in apertura, per richiesta del capo. Azioni: «Accedi» in apertura e «Parla con noi» in chiusura.
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

Fonti: duezero.eu, scheda App Store, pagina di login di hyperparts.it. La pagina di accesso di hyperparts.it (letta il 2026-10-07) offre: accesso con credenziali, recupero password, pulsante **DEMO**, **Request access** e accesso con **QR dall'app** («Or scan this code with the HyperParts app»). Il testo è in inglese. «Request access» porta a `https://hyperparts.it/RichiestaAcceso.aspx` (indirizzo diretto, collegabile dalla landing): è un **modulo per creare un account**, non un contatto commerciale; «Parla con noi» non va collegato lì. Gli altri pulsanti, DEMO compreso, sono azioni interne (`__doPostBack`), non indirizzi: dalla landing si può puntare a `https://hyperparts.it/` e al modulo di richiesta, non direttamente alla demo. `Dashboard.aspx` rimanda al login. La demo non è stata aperta (serve un clic dentro l'app).

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

## Struttura attuale di docs/index.html

1. **Navigazione**: fissa in alto, compare solo dopo l'apertura, con i soli link alle sezioni. Niente logo, nome né «Accedi».
2. **Apertura**: a tutto schermo. Foto di sfondo scelta a caso a ogni caricamento tra tre generate senza testo (blu alimentare, ambra bevande, verde farmaceutico, in `docs/assets/img/sfondi/`), con una sfumatura scura in basso perché SCROLL giallo si legga anche sui fondi chiari. A sinistra una scheda di accesso sollevata (32vw, tra 380 e 520 px), staccata dai bordi, con angoli arrotondati su tutti e quattro i lati e ombra, quasi a tutta altezza (margine di circa 2,6svh sopra e sotto; prova per vedere se piace più della colonna a tutta altezza). Sotto i 740px di altezza lo schermo l'illustrazione sparisce: logo e scritta dall'immagine `hp-pagina-avvio.png`, email, password, «Password dimenticata?» e «Accedi», una piccola vista esplosa stilizzata (`esploso.webp`, un solo pezzo giallo, fusa col fondo con `mix-blend-mode: multiply`), poi la parte gialla con «Richiedi accesso», il QR grande (segnaposto) e la frase. Il pulsante DEMO dell'originale non c'è. A destra la vela blu, come nella versione originale: curva concava, piatta in basso e ripida verso destra, con la punta al centro dello schermo (50%) e alta sul lato destro. In basso al centro dello schermo l'icona, la freccia gialla e la parola SCROLL gialla, sotto la punta. Sotto i 960px la scheda diventa una scheda sopra la foto (sotto i 768px senza illustrazione né QR). Nessun titolo visibile (resta un `h1` nascosto). Il form non autentica: svuota i campi e apre hyperparts.it, in attesa del codice dell'app.
2b. **Immagine del prodotto**: subito dopo l'apertura, su fondo blu che continua la vela (stesso `--cut`, senza stacco). L'immagine `apertura-dashboard-app.webp` parte in cornice (`inset 7% 16%`), si apre a tutta larghezza a metà percorso e si richiude prima del Capitolo 1 (GSAP + ScrollTrigger da cdnjs, scrub, solo senza `prefers-reduced-motion`). Senza didascalia in vetro. Sopra l'immagine, nella fascia blu, il claim provvisorio «Il ricambio giusto, al primo ordine.» in bianco su due righe, con a destra «Tavole ricambi legate alla matricola di ogni macchina, da browser e da app.» (prova: da confermare se piace e se il testo resta).
3. **Capitolo 1, Come si vede**: scena fissata a 5 passi (Inquadra il QR, Apre la matricola, Trova il ricambio, Controlla disponibilità e listino, Chiede il preventivo; testi provvisori), alta 500% dello schermo. Il telefono scorre tra le 3 schermate reali dell'App Store (i passi 4 e 5 riusano la terza). Ogni passo aggiunge un gruppo di sticker (13 immagini in `docs/assets/img/stickers/`, ripetute fino a 63 elementi): spuntano con un pop, a ondate sfalsate, e si impilano uno sull'altro ai lati, in alto e in basso, senza coprire il testo. Al momento dell'arrivo nel capitolo non c'è nessuno sticker: il primo gruppo spunta dopo circa 80px di scroll dentro la scena, gli altri a ogni passo. Il controllo che nessuno sticker tocchi capitolo, titolo, testo, scritta sotto il pallino e barra di avanzamento è stato fatto a 1280, 1440, 1920 e 375px. Sotto i 768px ne restano 15, più piccoli. Gli sticker sono pezzi del mondo dei ricambi (stile adesivo con retino, blu navy e giallo): niente mani, volti o simboli da pubblicità. Fascia laterale calcolata sul margine del testo (`--tl`).
4. **Capitolo 2, A chi serve** (rivisto il 2026-10-15): su carta, senza linea di separazione dal Capitolo 1. Il passaggio lo fanno 13 sticker a cavallo del confine (livello fuori dalla scena fissata, interi e non tagliati), sparsi in modo disordinato: tre nella fascia di sinistra, gli altri da metà pagina in poi, e alcuni più piccoli che scendono leggermente dentro il capitolo. Stanno lontani dal blocco di sinistra (barra di avanzamento e «Schermate provvisorie…» sopra, etichetta e titolo sotto). Controllo di contatto a numeri a 1100, 1280, 1440 e 2000px contro scritta sotto il pallino, barra, etichetta, titolo, intestazioni e celle della tabella. Fondo: puntini blu fissi (retino come negli sticker, navy al 30%, passo 13px) in alto, per circa 520–800px: sfumano da sopra (così non c'è una riga al confine con il Capitolo 1), hanno il picco poco sotto e si spengono lentamente verso la tabella; è un'eccezione alla regola «nessuna texture sul fondo». Fermo sullo schermo, per circa 190% dell'altezza dello schermo, c'è l'intero blocco: la fila di sticker del confine, l'etichetta, il titolo e la tabella. Si ferma più in basso possibile (con 28px sotto) così in alto resta visibile la parte bassa degli sticker, sotto la navbar (come nella foto di riferimento dell'utente). La posizione si calcola in JS dall'altezza del blocco; sugli schermi sotto i 900px di altezza la tabella si compatta (spazi e padding ridotti) perché il blocco ci stia. Ogni passo di scroll fa scattare una riga, a 25%, 70%, 115% e 160% dello schermo. All'inizio tutte le celle «Oggi» sono accese (blu navy, scritta bianca) e la parte «Con Hyper.Parts» è vuota; a ogni passo «Oggi» si oscura (blu quasi nero, scritta grigia, 0,8 s) e una striscia gialla piena si allunga dalla freccia quasi fino al bordo destro della pagina (1,1 s), mentre il testo nuovo compare solo quando arriva. Tornando indietro, la riga si riaccende. Se il blocco non ci sta nello schermo (sotto 768px di larghezza o in schermi molto bassi) non c'è il blocco: ogni riga scatta da sola quando entra in vista, con 0,4 s di attesa. Non dipende dall'hover, che non cambia più niente; senza JavaScript o con movimento ridotto si vede subito lo stato finale. Su telefono ogni ruolo è un blocco: blu sopra, giallo sotto. Testi provvisori.
5. **Capitolo 3, Come funziona**: su carta. Tre passaggi in colonna, ognuno con un segno «Passo N» e un'immagine illustrativa (manuale tecnico, monitor col disegno in vista esplosa, portatile con mappa e grafici), generate e non l'interfaccia vera.
6. **Capitolo 4, Domande**: quattro domande rapide con risposta visibile (accesso, cosa c'è per ogni macchina, rete, dispositivi), solo con fatti verificati.
7. **Capitolo 5, Due.Zero**: piccola sezione nera, testo chiaro, pallino rosso, link a duezero.eu.
8. **Capitolo 6, Contatti**: due percorsi separati da una riga. «Vuoi attivare Hyper.Parts?» con titolo, frase sull'accesso riservato e l'unica azione primaria «Parla con noi». «Accedi o richiedi l'accesso» con due pulsanti a contorno (Accedi, Richiedi accesso, che porta al modulo di richiesta dell'app) e sotto «Scarica l'app» con i badge ufficiali App Store e Google Play. Sotto, la vela blu e il footer con solo la riga del copyright.

Il pannello bozza è stato tolto dalla pagina. Le note per la revisione sono nel documento inviato al capo, non nel repo.

## Decisioni prese

- **Modo di comunicare**: affidabilità operativa («il ricambio giusto, al primo ordine»). Scartata la direzione sul valore economico.
- **Carattere dalla coreografia dello scroll e dalla scala tipografica**, non dal colore. Le scene che fissano lo scroll sono ammesse, come su duezero.eu.
- **Scena centrale**: tutto fermo, il testo si sostituisce, lo schermo scorre in verticale.
- **Apertura sostituita (2026-10-14, richiesta del capo)**: accesso a sinistra su foto di sfondo, vela blu ridotta, via titolo, immagine del prodotto che si allargava, logo e nome in alto, «Accedi» in navbar e «Parla con noi» sulla vela. Il logo passa in basso al centro con la freccia di scroll.
- **Pulsanti**: pillola in mono maiuscolo con `[+]`, il linguaggio di duezero.eu.
- **Passaggi tra sezioni**: etichetta «Capitolo N | titolo» con la sfera gialla.
- **La sfera** è il punto di Hyper.Parts e segna solo dove sei (logo, capitoli, avanzamento della scena). Non è un elenco puntato.
- **Il taglio del logo** come elemento riconoscibile: la curva che divide l'icona, separa la carta da una superficie di colore. Compare in chiusura e, ridotto a vela in basso a destra, in apertura (non nella scena del telefono).
- **Palette per ruoli**: struttura neutra (carta, inchiostro, nero), navy e giallo solo sul prodotto, rosso solo Due.Zero. Titoli in inchiostro, non più in blu.
- **Vela solo in apertura e nel footer**: tolta dalla scena del telefono, perché due curve ravvicinate si pestavano. Colore blu (il livello del logo), non grigio.
- **Due.Zero**: piccola sezione scura prima dei contatti. Nel testo «dal 2008», non «da oltre vent'anni». Niente frase bianca sulla vela nel footer.
- **Sezioni centrali**: «A chi serve» e «Come funziona» su carta, righe allineate, titoli di dimensione media. Meno tipografia: i titoli giganti in maiuscolo sono stati ridotti.
- **Sezioni centrali meno solo-testo**: la tabella di «A chi serve» ha colonne colorate e tono diretto; «Come funziona» ha tre immagini illustrative generate (prompt in `note/PROMPT-IMMAGINI.md`), con schermi sfocati e senza testo perché non mostrano l'interfaccia vera. Provati e tolti due ritagli della foto di apertura, che ripetevano la hero. Il footer non ha più la scritta «Bozza, testo provvisorio».
- **Obiettivo della pagina**: far percepire in fretta perché ha valore usare un software come questo. Le note per la revisione stanno nel documento inviato per email.
- **Nessuna sottolineatura**: né i segni del testo provvisorio né quelle dei link. I link d'azione sono pulsanti.
- **Niente quarta azione in chiusura**: i link dell'app sono i badge ufficiali, non pulsanti. Da chiedere al capo se richiesta di accesso e consulenza («Parla con noi») devono restare due azioni diverse.
- **Azioni con gerarchia** (aggiornata il 2026-10-14): in apertura «Accedi» è l'azione piena del pannello; in chiusura «Parla con noi» resta piena, le altre sono a contorno. Le azioni piene sono due, per richiesta del capo. Scartata: una sola azione primaria piena.

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
- **Vetro**: non più usato (era sul pannello di accesso, che ora è opaco come l'originale).
- **Nome**: «Hyper.Parts» o «HyperParts».
- **Destinazione di «Parla con noi»**: oggi `#contatti`, segnaposto.
- **Ritmo della parte centrale**: con «A chi serve» e «Come funziona» entrambe su carta e a righe, la parte centrale è calma; il contrasto viene da Due.Zero (nero) e dalla vela. Da rivalutare.
- **Due.Zero**: manca il logo; il rosso `#E2231A` è dedotto dal sito, da confermare come segno di Due.Zero.
- **Testo definitivo**: da ricevere. Il motivo di ogni sezione è nel documento per il capo.
- **Spunti da confermare con Due.Zero**: «ciascuno con la propria area» (passo «La crescita») e «video» tra i contenuti.

## Immagini

Le immagini sono in `docs/assets/img/`, scaricate dalle fonti pubbliche dell'azienda. Sono provvisorie: vanno sostituite con gli originali, solo con dati dimostrativi.

| File | Origine | Da chiedere |
|---|---|---|
| `app-01-home.webp`, `app-02-matricole.webp`, `app-03-scheda-macchina.webp` | schermate della scheda App Store | schermate originali |
| `blu-alimentare.webp`, `ambra-bevande.webp`, `verde-farmaceutico.webp` (1672×941) | generate con un'AI il 2026-10-14, senza testo; tre colori e tre settori | provvisorie: rigenerare più grandi (2560×1440) se serve nitidezza sugli schermi grandi |
| `hp-pagina-avvio.png` (420×551) | `hyperparts.it/immagini/HP_Pagina_Avvio.png` | sfondo della scheda di accesso: contiene logo e scritta, da confermare con l'azienda |
| `esploso.webp` (1619×469) | generata con un'AI il 2026-10-14, ritagliata al contenuto | illustrazione di fantasia, non un disegno tecnico reale di una macchina |
| mancante | | schermata desktop della tavola ricambi, eventuale registrazione breve |

In `docs/assets/`:

- `hyperparts-icona-originale.svg`: file ricevuto, contiene sovrapposti lo stato a riposo e quello al passaggio del mouse.
- `hyperparts-icona.svg`: solo lo stato a riposo, ricavato dall'originale.
- `hyperparts-icona-hover.svg`: solo lo stato al passaggio del mouse.

Il logo è l'icona. In pagina il nome è composto in testo, con la sfera al posto del punto.

## Note tecniche

- Gli stati iniziali delle animazioni si applicano solo sotto `html.js:not(.reduce)`: senza JavaScript o con movimento ridotto la pagina è già nello stato finale.
- Nessun listener di `scroll`: si usano `IntersectionObserver` e `position: sticky`. La scena cambia passo con tre sentinelle e `rootMargin: '-49% 0px -49% 0px'`.
- `IntersectionObserver` non rileva un elemento ritagliato del tutto da `clip-path`: si osserva il contenitore.
- La vela dell'apertura è un `<svg>` con `preserveAspectRatio="none"` e un solo tracciato: cuneo con punta sul bordo basso, al centro. Con una maschera CSS la punta restava piatta e si vedeva solo molto più a destra. Il taglio in chiusura e nel footer resta il cerchio di 400vw dentro `.cut-host`.
- Sotto i 768px il QR si nasconde (serve a inquadrare dall'app da un altro schermo) e la vela si riduce.

## Non verificato

Fluidità del movimento su un browser vero, tocco su telefono reale, Safari e Firefox, `prefers-reduced-motion`. Controllati solo a schermo, a 1024px e 375px, in un browser basato su Chromium: struttura, passi della scena, assenza di scorrimento orizzontale e di errori in console.
