# Piano di studio AI-200

Sep 28, 2026 · @MeepleAiAdmin

## Panoramica

L'obiettivo è superare l'esame AI-200 (servono almeno 700 punti su 1000) intorno al Jan 12, 2027. Con 1–2 ore al giorno, weekend incluso, sono 7–14 ore a settimana: circa 140 ore in 15 settimane.

&#91;embedded content: piano AI-200 · 4 fasi, esame a gennaio 2027\]

Python e Azure si sovrappongono nella terza settimana. L'ultima fase cade durante le feste di Natale, per questo dura tre settimane: c'è margine per i giorni saltati.

## Come organizzare la settimana

Nei giorni feriali si studia la teoria, nel weekend si mette tutto in pratica su Azure.

| Giorno | Tempo | Cosa fare |
| --- | --- | --- |
| Lun–Ven | 1 ora | 45 minuti di teoria (moduli Microsoft Learn), 15 minuti di appunti e domande di ripasso |
| Sabato | 2 ore | Laboratorio: aggiungi al progetto pratico il pezzo studiato in settimana |
| Domenica | 1–2 ore | Finisci il laboratorio, poi 20 minuti di ripasso della settimana |

- Se salti un giorno, non raddoppiare il giorno dopo: recupera nel weekend.
- Tieni un file "errori" con ogni domanda sbagliata e il perché. Nelle ultime settimane è il materiale di ripasso più utile.
- Quando una sera sei stanco, fai solo i 15 minuti di ripasso. Mantenere l'abitudine conta più della singola sessione.

## Fase 1 — Python per chi viene da C# (settimane 1–3)

Non devi diventare esperto di Python: ti basta leggere e scrivere script che usano gli SDK di Azure. Usa VS Code con l'estensione Python e Python 3.12 o successivo.

1. **Settimana 1 — le basi.** Variabili e tipi, `list`/`dict`/`set`, cicli, funzioni, f-string, list comprehension. Crea un ambiente virtuale (`python -m venv .venv`) e installa i pacchetti con `pip`.
2. **Settimana 2 — strutture.** Classi, `@dataclass`, eccezioni, moduli e pacchetti, type hint, `with`, lettura di file e JSON, chiamate HTTP con `requests`.
3. **Settimana 3 — async e primo SDK Azure.** `async def`/`await` con `asyncio`, `logging`, variabili d'ambiente. Esercizio finale: uno script che legge un segreto da Key Vault con `azure-identity` (`DefaultAzureCredential`) e `azure-keyvault-secrets`.

**Traduzioni utili da C#:**

| C# | Python |
| --- | --- |
| `using (var x = ...)` | `with ... as x:` |
| LINQ `Where`/`Select` | list comprehension `[f(x) for x in xs if cond]` |
| `List<T>`, `Dictionary<K,V>` | `list`, `dict` |
| `$"Ciao {nome}"` | `f"Ciao {nome}"` |
| `async Task` + `await` | `async def` + `await`, avvio con `asyncio.run()` |
| NuGet, `.csproj` | pip, `requirements.txt` o `pyproject.toml` |
| `try/catch/finally` | `try/except/finally` |

**Fatto quando:** riesci a scrivere senza aiuto uno script async che chiama un'API REST, gestisce gli errori e legge la configurazione da variabili d'ambiente.

## Fase 2 — Basi di Azure e Docker (settimane 3–5)

Queste sono le basi che l'AI-200 dà per scontate. Studia il materiale del percorso AZ-900 su Microsoft Learn senza sostenere quell'esame, e aggiungi Docker.

1. **Settimana 3 — come è fatto Azure.** Tenant, subscription, resource group, regioni. Crea l'account gratuito e imposta subito un budget con avviso. Installa la Azure CLI (`az`) e crea ed elimina risorse da riga di comando.
2. **Settimana 4 — identità e accessi.** Entra ID, ruoli RBAC, service principal e soprattutto **managed identity**: all'esame torna in quasi tutte le aree. Capisci cosa fa `DefaultAzureCredential` in locale e in cloud.
3. **Settimana 5 — Docker.** Dockerfile, build multi-stage, variabili d'ambiente, `docker run` con porte e volumi, un `docker compose` con app e database. Metti in un container lo script Python della fase 1.

**Fatto quando:** crei un resource group con la CLI, fai girare in locale un container con un'app Python e sai spiegare perché una managed identity è meglio di una connection string.

## Fase 3 — Le quattro aree d'esame (settimane 6–12)

Le sette settimane seguono i pesi della guida ufficiale. I dati per l'AI, l'area che pesa di più (25–30%), hanno più spazio.

| Settimana | Area (peso) | Cosa studiare | Laboratorio del weekend |
| --- | --- | --- | --- |
| 6 · dal 2 nov | Container (20–25%) | Azure Container Registry, `az acr build`, App Service per container, Container Apps | Pubblica l'app su Container Apps prendendo l'immagine da ACR |
| 7 · dal 9 nov | Container (20–25%) | AKS di base e `kubectl`, revisioni e scaling in Container Apps, log ed eventi per il troubleshooting | Rompi di proposito un deploy e trova l'errore nei log |
| 8 · dal 16 nov | Dati per l'AI (25–30%) | Cosmos DB for NoSQL: SDK, partition key, consistenza, embedding vettoriali e ricerca per similarità | Salva documenti con embedding in Cosmos DB e cerca i più simili |
| 9 · dal 23 nov | Dati per l'AI (25–30%) | PostgreSQL con `pgvector`, schema RAG, filtri sui metadati | Stessa ricerca su PostgreSQL, poi confronta i due approcci |
| 10 · dal 30 nov | Dati per l'AI + Servizi | Azure Managed Redis (cache e indici vettoriali), Azure Functions (trigger, binding, API serverless) | Metti una cache Redis davanti alla ricerca, esponi un endpoint con una Function |
| 11 · dal 7 dic | Servizi (20–25%) | Service Bus (code e topic), Event Grid, quando usare l'uno o l'altro | Il caricamento di un documento genera un evento che avvia l'indicizzazione |
| 12 · dal 14 dic | Sicurezza e monitoraggio (20–25%) | Key Vault, App Configuration, OpenTelemetry e Application Insights, query KQL | Sposta tutti i segreti in Key Vault, aggiungi il tracing e scrivi 5 query KQL |

Alla fine di ogni settimana apri la guida ufficiale e spunta le voci che sapresti spiegare a un collega. Quelle che restano scoperte finiscono nel ripasso.

## Fase 4 — Ripasso, simulazioni ed esame (settimane 13–15)

Prenota l'esame intorno al Dec 7, 2026 per il 12 gennaio. Una data fissata aiuta a restare costante durante le feste.

1. **Settimana 13 · dal 21 dic.** Fai la practice assessment gratuita di Microsoft Learn come punto di partenza, senza prepararti. Individua le due aree più deboli e ristudiale.
2. **Settimana 14 · feste.** Ritmo più leggero: rileggi il file "errori" e rifai i laboratori delle aree deboli.
3. **Settimana 15 · dal 4 gen.** Rifai la practice assessment. Prova l'interfaccia d'esame con l'exam sandbox di Microsoft.

**Pronto quando:** superi con costanza l'80% nelle simulazioni. Se non ci arrivi, sposta l'esame di una o due settimane invece di presentarti impreparato.

Per gli esami role-based Microsoft permette di consultare Microsoft Learn durante la prova. Prima di prenotare, verifica che valga anche per l'AI-200.

## Progetto pratico

Conviene costruire un unico progetto per tutte le settimane: una piccola ricerca semantica (RAG) sui tuoi documenti o manuali. Ogni laboratorio del weekend aggiunge un pezzo, e a fine dicembre avrai toccato quasi tutto il programma.

&#91;embedded content: progetto pratico · architettura\]

Il caricamento passa dalla coda alla Function, che calcola gli embedding e li salva. La ricerca prova prima Redis e poi il database vettoriale. Metti il codice su GitHub: è anche un buon esempio da mostrare nei colloqui.

## Risorse e costi

**Risorse principali:**

- [Guida di studio ufficiale AI-200](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200): l'elenco completo delle competenze, da usare come checklist.
- Microsoft Learn: moduli gratuiti, sandbox, practice assessment ed exam sandbox.
- Account gratuito di Azure per i laboratori del weekend.

**Per tenere bassi i costi:**

- Imposta un budget con avviso via email la prima settimana.
- Crea un resource group per ogni laboratorio e cancellalo a fine sessione con `az group delete`.
- Preferisci i piani gratuiti o serverless: il free tier di Cosmos DB, Functions a consumo, Container Apps con scale-to-zero.
- AKS e Redis costano anche quando non li usi: creali e cancellali nello stesso giorno.

**Fonte:** [Microsoft Learn — Study guide for Exam AI-200](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200)
