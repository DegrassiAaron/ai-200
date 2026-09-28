# search

La ricerca semantica: da una domanda in linguaggio naturale ai documenti più vicini.

**Settimana 08** — Cosmos DB. **Settimana 09** — PostgreSQL con pgvector. **Settimana 10** — cache Redis.

## Da costruire

Una sola interfaccia di ricerca e due implementazioni dietro, così puoi confrontarle:

- **Cosmos DB for NoSQL**: salvataggio degli embedding, ricerca per similarità, scelta della
  partition key, effetto della indexing policy sul consumo di RU.
- **PostgreSQL con pgvector**: schema, indice vettoriale, filtri sui metadati, ottimizzazione delle
  connessioni.
- **Redis davanti a entrambe**: cache dei risultati, scadenza, invalidazione quando un documento
  cambia. Poi l'indice vettoriale su Redis stesso, che è la seconda voce d'esame sul servizio.

## Fatto quando

La stessa query gira sui due database e sai dire, con i numeri sotto gli occhi, come cambiano
latenza e costo. Il confronto va negli appunti della settimana 09.
