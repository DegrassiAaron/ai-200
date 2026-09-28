# functions

Le Azure Functions del progetto: consumano la coda, calcolano gli embedding, li scrivono nel
database vettoriale, ed espongono la ricerca come API serverless.

**Settimana 10** — trigger, binding, configurazione e deploy. **Settimana 11** — trigger da Service Bus.

## Da costruire

- Function con trigger da coda Service Bus: legge il riferimento al documento, calcola gli
  embedding, li scrive nel database vettoriale.
- Function con trigger HTTP che espone la ricerca.
- Binding di input e output invece del codice di connessione scritto a mano, dove possibile: la
  differenza fra trigger e binding è materia d'esame.
- Configurazione e deploy della function app.

## Fatto quando

La function app è in esecuzione su Azure, si autentica con managed identity, e la ricerca risponde
da un endpoint pubblico senza segreti nel codice.
