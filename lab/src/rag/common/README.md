# common

Codice condiviso fra `ingest`, `functions` e `search`. Qui non va logica di dominio.

| Cosa | Settimana | Stato |
| --- | --- | --- |
| `config.py` — configurazione dall'ambiente | 03 | fatto |
| `identity.py` — `DefaultAzureCredential` e client autenticati | 04 | da scrivere |
| `secrets.py` — lettura dei segreti da Key Vault | 03 · 12 | da scrivere |
| `telemetry.py` — tracing OpenTelemetry verso Application Insights | 12 | da scrivere |

## identity.py — settimana 04

Una funzione che restituisce la credenziale da usare ovunque, così nessun altro modulo sa come ci
si autentica. Il punto da capire, perché all'esame ritorna: `DefaultAzureCredential` prova le fonti
in ordine, e in locale finisce sull'Azure CLI mentre in cloud usa la managed identity.

**Fatto quando:** lo stesso codice gira in locale e su Container Apps senza una sola connection
string nel repository.

## secrets.py — settimane 03 e 12

Nella settimana 03 è l'esercizio finale della Fase 1: leggere un segreto da Key Vault con
`azure-identity` e `azure-keyvault-secrets`. Nella settimana 12 diventa il modo in cui tutto il
progetto prende i suoi segreti, rotazione compresa.

## telemetry.py — settimana 12

Inizializzazione di OpenTelemetry, span sulle operazioni di ricerca e indicizzazione, correlazione
fra ingest e function.

**Fatto quando:** in Application Insights vedi una traccia sola che parte dall'upload e arriva alla
scrittura dell'embedding, e sai scrivere la query KQL che la trova.
