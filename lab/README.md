# lab — ricerca semantica (RAG) su Azure

Il progetto pratico del piano di studio. Un solo progetto per tutte le settimane: ogni laboratorio
del weekend aggiunge un pezzo, e a fine dicembre avrà toccato quasi tutto il programma d'esame.

**Cosa fa, a regime:** carichi un documento, questo finisce su una coda; una Function calcola gli
embedding e li salva in un database vettoriale; la ricerca interroga prima la cache e poi il
database.

## Il flusso

```
        upload
          |
          v
   [ ingest ] --messaggio--> Service Bus --trigger--> [ functions ]
                                                            |
                                                       embedding
                                                            |
                                                            v
                                            Cosmos DB / PostgreSQL + pgvector
                                                            ^
        query --> [ search ] --> Redis (cache) -------------+
```

Trasversali a tutto: Key Vault per i segreti, App Configuration, tracing OpenTelemetry verso
Application Insights.

## Cosa aggiunge ogni weekend

| Sett. | Componente | Laboratorio |
| --- | --- | --- |
| 05 | `Dockerfile` | Mettere in container lo script della Fase 1 |
| 06 | — | Pubblicare l'immagine su ACR e l'app su Container Apps |
| 07 | — | Rompere un deploy di proposito e trovarlo nei log |
| 08 | `search`, `functions` | Documenti con embedding su Cosmos DB, ricerca per similarità |
| 09 | `search`, `functions` | Stessa ricerca su PostgreSQL con pgvector, poi confronto |
| 10 | `search`, `functions` | Cache Redis davanti alla ricerca, endpoint con una Function |
| 11 | `ingest`, `functions` | L'upload genera un evento che avvia l'indicizzazione |
| 12 | `common` | Segreti in Key Vault, tracing, cinque query KQL |

## Cosa c'è già

Solo l'impalcatura, perché scrivere il resto **è** l'esercizio:

- `pyproject.toml` con un gruppo di dipendenze per fase — installa solo quelle della settimana in corso.
- `src/rag/common/config.py`: lettura della configurazione dall'ambiente, con i due helper
  (`required`, `optional`) che riuserai per ogni servizio che aggiungi.
- `src/rag/__main__.py`: carica la configurazione e la stampa. Serve a verificare che l'ambiente sia
  a posto, in locale e dentro il container.
- `Dockerfile` multi-stage funzionante, da riscrivere nella settimana 05.
- `tests/` con i test della configurazione, come modello per i tuoi.

Ogni sottocartella di `src/rag/` ha un README con cosa costruire, in quale settimana, e il criterio
per dire che è finito.

## Come si parte

```powershell
cd lab
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
Copy-Item .env.example .env
python -m rag
pytest
```

Nel container:

```powershell
docker build -t rag-lab .
docker run --rm --env-file .env rag-lab
```

## Igiene sui costi

Un resource group per laboratorio, cancellato a fine sessione. Gli script stanno in `infra/`.
