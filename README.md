# AI-200 — Developing AI Cloud Solutions on Azure

Preparazione all'esame Microsoft **AI-200**. Soglia di superamento: 700 su 1000.
Data obiettivo: **12 gennaio 2027**.

## Dove sta cosa

| Percorso | A cosa serve |
| --- | --- |
| [`Piano di studio AI-200.md`](<Piano di studio AI-200.md>) | Il piano: 4 fasi, ritmo settimanale, laboratori, costi |
| [`checklist-competenze.md`](checklist-competenze.md) | Le competenze della guida ufficiale, una casella per voce |
| [`errori.md`](errori.md) | Domande sbagliate, perché, e i punteggi delle simulazioni |
| [`appunti/`](appunti/) | Un file per settimana, già intestato con gli argomenti del piano |
| [`lab/`](lab/) | Il progetto pratico: ricerca semantica (RAG) sui propri documenti |

## Ritmo settimanale

| Giorno | Tempo | Cosa fare |
| --- | --- | --- |
| Lun–Ven | 1 ora | 45 minuti di teoria, 15 minuti di appunti e ripasso |
| Sabato | 2 ore | Laboratorio in `lab/`: aggiungi il pezzo studiato in settimana |
| Domenica | 1–2 ore | Finisci il laboratorio, poi 20 minuti di ripasso |

Un giorno saltato si recupera nel weekend, non raddoppiando il giorno dopo.

## Il giro completo

1. **Lun–Ven** — teoria, appunti in `appunti/<fase>/settimana-NN-*.md` sotto *Appunti*.
   Quello che non torna va sotto *Domande aperte*.
2. **Weekend** — laboratorio in `lab/`, un componente per settimana.
3. **Fine settimana** — apri `checklist-competenze.md` e spunta solo quello che sapresti spiegare
   a un collega. Il resto va in `errori.md`.
4. **Settimane 13–15** — `errori.md` diventa il materiale di ripasso principale.

## Fasi

| Fase | Settimane | Contenuto |
| --- | --- | --- |
| 1 | 1–3 | Python per chi viene da C# |
| 2 | 3–5 | Basi di Azure (materiale AZ-900) e Docker |
| 3 | 6–12 | Le quattro aree d'esame, nell'ordine dei pesi ufficiali |
| 4 | 13–15 | Ripasso, simulazioni, esame |

## Costi

Il piano prevede l'account gratuito di Azure. Per non superarlo:

- Budget con avviso via email, impostato la prima settimana.
- Un resource group per laboratorio, cancellato a fine sessione con `az group delete`.
- Piani gratuiti o serverless: free tier di Cosmos DB, Functions a consumo, Container Apps con
  scale-to-zero.
- AKS e Redis costano anche da fermi: creali e cancellali nello stesso giorno.

## Fonte

[Microsoft Learn — Study guide for Exam AI-200](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200)
