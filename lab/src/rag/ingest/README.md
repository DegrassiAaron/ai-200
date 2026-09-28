# ingest

Riceve un documento e lo mette in coda. Non calcola embedding e non scrive sul database: il suo
unico lavoro è accettare il file e produrre un messaggio.

**Settimana 11** — Service Bus ed Event Grid.

## Da costruire

- Endpoint o comando che accetta un documento e lo salva nello storage.
- Messaggio su una coda Service Bus con il riferimento al documento.
- Gestione della dead-letter queue: cosa succede a un documento che fallisce ripetutamente.
- In alternativa, un evento Event Grid. Prova entrambi e scrivi negli appunti quando conviene l'uno
  e quando l'altro: è esattamente la distinzione che l'esame chiede sotto forma di scenario.

## Fatto quando

Carichi un documento, il messaggio compare in coda, la function parte da sola, e un documento
malformato finisce in dead-letter invece di bloccare la coda.
