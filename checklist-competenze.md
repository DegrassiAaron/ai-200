# Checklist competenze AI-200

Le voci qui sotto sono la traduzione della sezione *Skills measured* della
[guida ufficiale](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200)
(pagina aggiornata il 15 aprile 2026). I nomi dei servizi restano in inglese perché così compaiono
nel portale e nelle domande d'esame.

**Convenzione:** spunta una voce solo quando la sapresti spiegare a un collega senza guardare gli
appunti. Le voci rimaste scoperte a fine settimana finiscono in `errori.md`.

I riferimenti `sett. N` rimandano alla Fase 3 del `Piano di studio AI-200.md`.

---

## 1. Develop containerized solutions on Azure — 20–25%

### Container application hosting · sett. 6

- [ ] Costruire, archiviare, versionare e gestire immagini con **Azure Container Registry**
- [ ] Costruire ed eseguire immagini con **ACR Tasks** (`az acr build`)
- [ ] Distribuire container su **Azure App Service**, configurando variabili d'ambiente e segreti

### Soluzioni orchestrate · sett. 7

- [ ] Distribuire applicazioni su **Azure Container Apps**: configurazione dell'environment e gestione delle revisioni
- [ ] Implementare lo scaling event-driven con **KEDA** in Container Apps
- [ ] Distribuire e gestire applicazioni su **AKS** tramite file manifest
- [ ] Monitorare e risolvere problemi su AKS e Container Apps leggendo log, eventi e connettività end-to-end

---

## 2. Develop AI solutions by using Azure data management services — 25–30%

### Azure Cosmos DB for NoSQL · sett. 8

- [ ] Connettersi a Cosmos DB for NoSQL con l'SDK ed eseguire query
- [ ] Ottimizzare performance e consumo di **Request Unit (RU)** con indexing policy e livelli di consistenza
- [ ] Salvare e recuperare **embedding** ed eseguire ricerca per similarità vettoriale
- [ ] Implementare un **change feed processor** per intercettare item nuovi o modificati

### Azure Database for PostgreSQL · sett. 9

- [ ] Connettersi e interrogare PostgreSQL tramite SDK
- [ ] Modellare lo schema e scegliere i tipi di dato adatti
- [ ] Strategie di indicizzazione: ridurre la latenza delle query e il costo computazionale di **pgvector**
- [ ] Dimensionare compute, memoria e storage per carichi vettoriali
- [ ] Ricerca per similarità: salvare embedding, recupero semantico, pattern **RAG** con filtri sui metadati
- [ ] Ottimizzare le connessioni per aumentare il throughput e ridurre la latenza

### Azure Managed Redis · sett. 10

- [ ] Operazioni sui dati: caching, scadenza (expiration) e invalidazione
- [ ] Indicizzazione vettoriale per la ricerca per similarità

---

## 3. Connect to and consume Azure services — 20–25%

### Soluzioni a eventi e messaggi · sett. 11

- [ ] Accodare ed elaborare operazioni di back-end con **Azure Service Bus**: code, topic, subscription e **dead-letter queue**
- [ ] Implementare workflow event-driven con **Azure Event Grid**: filtri, eventi custom, retry

### Azure Functions · sett. 10

- [ ] Costruire API serverless con **trigger** e **binding**
- [ ] Configurare e distribuire una function app

---

## 4. Secure, monitor, and troubleshoot Azure solutions — 20–25%

### Sicurezza · sett. 12

- [ ] Proteggere i segreti con **Azure Key Vault**: rotazione e recupero
- [ ] Salvare e leggere configurazione applicativa con **Azure App Configuration**

### Monitoraggio · sett. 12

- [ ] Tracciare sistemi distribuiti con gli SDK **OpenTelemetry**
- [ ] Scrivere query **KQL** per analizzare log e metriche

---

## Prerequisiti impliciti

Non sono un dominio d'esame, ma la guida li dà per scontati nel profilo del candidato
(Fasi 1 e 2 del piano).

- [ ] Python: sintassi, tipi, classi, `async`/`await`, gestione errori, package e virtual environment
- [ ] SDK Azure per Python e SDK di terze parti usati su Azure
- [ ] Modello di risorse Azure: tenant, subscription, resource group, regioni
- [ ] Azure CLI (`az`) per creare ed eliminare risorse
- [ ] Entra ID, ruoli RBAC, service principal e **managed identity**
- [ ] `DefaultAzureCredential`: come si comporta in locale e in cloud
- [ ] Docker: Dockerfile, build multi-stage, variabili d'ambiente, volumi, `docker compose`

---

**Fonte:** [Microsoft Learn — Study guide for Exam AI-200](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200)
