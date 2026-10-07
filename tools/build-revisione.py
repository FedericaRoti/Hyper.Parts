#!/usr/bin/env python3
"""Genera revisione/index.html: la pagina di index.html con il pannello «Note per la revisione».
Uso: python3 tools/build-revisione.py   (dalla radice del repo)"""
import json, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'index.html').read_text(encoding='utf-8')

GENERALI = [
  "Dopo trenta secondi, chi arriva capisce perché conviene usare un software così?",
  "Il nome: Hyper.Parts, HyperParts o Hyperparts? (c'è una nota con tutte le forme in uso)",
  "I colori: struttura in carta, inchiostro e nero, navy e giallo solo sul prodotto, rosso solo per Due.Zero. Funziona?",
  "Tutto il testo è provvisorio: serve una versione scritta da voi.",
]
SEZIONI = [
  {"id":"top","titolo":"Apertura",
   "perche":"Dice in una frase cosa fa Hyper.Parts e mostra subito il prodotto vero. «Accedi» resta sempre in alto per chi ha già le credenziali.",
   "domande":["«Il ricambio giusto, al primo ordine» fa capire il valore in pochi secondi?",
              "Serve un dato in apertura? Su duezero.eu c'è «il post-vendita può valere oltre il 20% del fatturato, con margini elevati»: lo usiamo, e con quale fonte?",
              "La foto è provvisoria: abbiamo l'originale? È una foto o un fotomontaggio?"]},
  {"id":"come-si-vede","titolo":"Come si vede",
   "perche":"Mostra in tre passi come lo usa un tecnico: QR, matricola, ricambio.",
   "domande":["Il percorso QR, matricola, ricambio è quello reale?",
              "Le schermate vengono dallo store: ci sono quelle originali?",
              "Tra i contenuti di ogni macchina compaiono anche i video: confermate?"]},
  {"id":"a-chi-serve","titolo":"A chi serve",
   "perche":"Quattro ruoli, ognuno in una riga: «Oggi» a sinistra, «Con Hyper.Parts» in risalto. I titoli parlano direttamente a chi legge («Se sei un tecnico in campo»), così ci si riconosce.",
   "domande":["Sono i ruoli giusti, nell'ordine giusto? Ne manca qualcuno?",
              "Le frasi «Oggi» sono realistiche per i vostri clienti? Il tono diretto («Se sei…») va bene o preferite i nomi dei ruoli?",
              "«Report sui componenti più soggetti a usura» è una funzione che Hyper.Parts ha davvero? Non è tra i fatti verificati."]},
  {"id":"come-funziona","titolo":"Come funziona",
   "perche":"Chiarisce che è un servizio gestito con Due.Zero, non un prodotto da attivare da soli.",
   "domande":["I tre passi corrispondono al processo vero (disegni CAD, distinte base, documentazione)?",
              "«Ciascuno con la propria area»: è corretto per ogni cliente del costruttore?",
              "Le tre immagini sono illustrative (generate, non l'interfaccia vera): vanno bene o preferite foto e schermate reali?"]},
  {"id":"domande","titolo":"Domande",
   "perche":"Risponde a quello che ci si chiede prima di scrivere: come si entra, cosa c'è, serve la rete, su cosa si usa.",
   "domande":["Quali domande arrivano davvero ai commerciali? Ne aggiungiamo?",
              "La risposta sull'accesso riservato è corretta?"]},
  {"id":"due-zero","titolo":"Due.Zero",
   "perche":"Dice chi c'è dietro, in poche righe e senza rimandare ad altri prodotti.",
   "domande":["«Dal 2008» è la formula giusta?",
              "Quanto brand Due.Zero mostrare? Il rosso e il pallino sono giusti? Abbiamo il logo?"]},
  {"id":"contatti","titolo":"Contatti",
   "perche":"Due percorsi separati: chi vuole attivare Hyper.Parts (Parla con noi) e chi lo usa già o deve entrare (Accedi, Richiedi accesso, app).",
   "domande":["Richiesta di accesso e consulenza devono essere due azioni diverse? Oggi «Parla con noi» è il contatto per la consulenza e «Richiedi accesso» porta al modulo per creare un account.",
              "Dove deve portare «Parla con noi»: modulo, email o telefono?",
              "Chi attiva gli account richiesti dal modulo «Richiedi accesso»: Due.Zero o il costruttore?",
              "Aggiungiamo «Guarda la demo»? Oggi la demo ha pagine che non funzionano e non ha un indirizzo diretto.",
              "Serve altro per chi non ha le credenziali?"]},
]

css = r'''
/* Pannello di revisione: non fa parte del sito */
.rv-btn { position: fixed; right: 16px; bottom: calc(16px + env(safe-area-inset-bottom, 0px)); z-index: 90; display: inline-flex; align-items: center; gap: 10px; min-height: 48px; padding: 12px 20px; border: 0; border-radius: 999px; background: var(--ink); color: var(--light); font: 500 13px/1 var(--mono); letter-spacing: .06em; text-transform: uppercase; cursor: pointer; box-shadow: 0 8px 24px -8px rgb(20 20 18 / .5); }
.rv-btn .sphere { width: 10px; height: 10px; }
.rv-panel { position: fixed; top: 0; right: 0; bottom: 0; z-index: 95; width: min(400px, 100vw); display: flex; flex-direction: column; background: var(--ink); color: rgb(250 250 247 / .88); transform: translateX(104%); transition: transform .45s var(--ease); box-shadow: -12px 0 40px -12px rgb(20 20 18 / .5); }
.rv-panel.open { transform: none; }
.rv-head { display: flex; align-items: flex-start; justify-content: space-between; gap: 16px; padding: calc(18px + env(safe-area-inset-top, 0px)) 20px 14px; border-bottom: 1px solid rgb(250 250 247 / .18); }
.rv-head h2 { margin: 0 0 4px; font: 800 24px/1 var(--display); color: var(--light); }
.rv-head p { margin: 0; font-size: 13px; line-height: 1.4; color: rgb(250 250 247 / .65); }
.rv-close { flex: none; width: 40px; height: 40px; border: 1px solid rgb(250 250 247 / .35); border-radius: 50%; background: transparent; color: var(--light); font: 500 16px/1 var(--mono); cursor: pointer; }
.rv-body { flex: 1; overflow-y: auto; padding: 8px 20px calc(24px + env(safe-area-inset-bottom, 0px)); }
.rv-block { padding-block: 16px; border-bottom: 1px solid rgb(250 250 247 / .14); }
.rv-block h3 { margin: 0 0 8px; }
.rv-go { display: inline-flex; align-items: center; gap: 8px; padding: 0; border: 0; background: none; color: var(--light); font: 800 20px/1.1 var(--display); text-align: left; cursor: pointer; }
.rv-go .sphere { width: 10px; height: 10px; opacity: 0; transition: opacity .25s ease; }
.rv-block.on .rv-go .sphere { opacity: 1; }
.rv-label { margin: 10px 0 4px; font: 500 11px/1 var(--mono); letter-spacing: .08em; text-transform: uppercase; color: rgb(250 250 247 / .55); }
.rv-block p { margin: 0; font-size: 14px; line-height: 1.5; }
.rv-block ul { margin: 0; padding-left: 18px; font-size: 14px; line-height: 1.5; }
.rv-block li + li { margin-top: 6px; }
.rv-btn:focus-visible, .rv-close:focus-visible, .rv-go:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }
@media (prefers-reduced-motion: reduce) { .rv-panel { transition: none; } }
'''

def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
blocks = ['<div class="rv-block"><h3 class="rv-go" style="cursor:default">Domande per tutta la pagina</h3><ul>' + ''.join(f'<li>{esc(d)}</li>' for d in GENERALI) + '</ul></div>']
for n in SEZIONI:
    blocks.append(
      f'<div class="rv-block" data-rv="{n["id"]}"><h3><button class="rv-go" type="button" data-target="{n["id"]}"><span class="sphere" aria-hidden="true"></span>{esc(n["titolo"])}</button></h3>'
      f'<p class="rv-label">Perché c’è</p><p>{esc(n["perche"])}</p>'
      f'<p class="rv-label">Da guardare e decidere</p><ul>' + ''.join(f'<li>{esc(d)}</li>' for d in n["domande"]) + '</ul></div>')

html = f'''
<button class="rv-btn" id="rv-open" type="button" aria-expanded="false" aria-controls="rv-panel"><span class="sphere" aria-hidden="true"></span>Note per la revisione</button>
<aside class="rv-panel" id="rv-panel" aria-label="Note per la revisione">
  <div class="rv-head"><div><h2>Note per la revisione</h2><p>Perché c’è ogni sezione e cosa guardare. Il pannello non fa parte del sito.</p></div><button class="rv-close" id="rv-close" type="button" aria-label="Chiudi le note">X</button></div>
  <div class="rv-body">{''.join(blocks)}</div>
</aside>
'''

js = r'''
(function () {
  var panel = document.getElementById('rv-panel'), openBtn = document.getElementById('rv-open'), closeBtn = document.getElementById('rv-close');
  function setOpen(o) { panel.classList.toggle('open', o); openBtn.setAttribute('aria-expanded', o ? 'true' : 'false'); if (o) closeBtn.focus(); else openBtn.focus(); }
  openBtn.addEventListener('click', function () { setOpen(!panel.classList.contains('open')); });
  closeBtn.addEventListener('click', function () { setOpen(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && panel.classList.contains('open')) setOpen(false); });
  document.querySelectorAll('.rv-go[data-target]').forEach(function (b) {
    b.addEventListener('click', function () {
      var el = document.getElementById(b.dataset.target); if (!el) return;
      el.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
      if (innerWidth < 900) setOpen(false);
    });
  });
  if ('IntersectionObserver' in window) {
    var blocks = {}; document.querySelectorAll('[data-rv]').forEach(function (b) { blocks[b.dataset.rv] = b; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        Object.keys(blocks).forEach(function (k) { blocks[k].classList.toggle('on', k === e.target.id); });
        if (panel.classList.contains('open') && blocks[e.target.id]) blocks[e.target.id].scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });
    Object.keys(blocks).forEach(function (k) { var el = document.getElementById(k); if (el) io.observe(el); });
  }
})();
'''
out = src.replace('</style>\n</head>', css + '</style>\n</head>', 1)
out = out.replace('<title>Hyper.Parts</title>', '<title>Hyper.Parts revisione</title>', 1)
out = out.replace('</body>', html + '<script>' + js + '</script>\n</body>', 1)
out = out.replace('src="assets/', 'src="../assets/').replace('href="assets/', 'href="../assets/')
d = root / 'revisione'; d.mkdir(exist_ok=True)
(d / 'index.html').write_text(out, encoding='utf-8')
(root / 'docs' / 'DOMANDE-PER-IL-CAPO.md').write_text(
  '# Domande per il capo\n\nStessi contenuti del pannello «Note per la revisione» della versione navigabile.\n\n## Per tutta la pagina\n' +
  ''.join(f'- {d_}\n' for d_ in GENERALI) + ''.join(
  f'\n## {n["titolo"]}\n**Perché c\'è.** {n["perche"]}\n\n**Da guardare e decidere**\n' + ''.join(f'- {d_}\n' for d_ in n["domande"]) for n in SEZIONI), encoding='utf-8')
print('ok')
