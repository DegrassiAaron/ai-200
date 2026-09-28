# infra

Gli script per creare e — soprattutto — cancellare le risorse di ogni laboratorio.

La regola del piano: **un resource group per laboratorio, cancellato a fine sessione.** AKS e Redis
costano anche da fermi, quindi vanno creati e cancellati nello stesso giorno.

```bash
az group create --name rg-ai200-sett08 --location westeurope
# ... il laboratorio ...
az group delete --name rg-ai200-sett08 --yes --no-wait
```

## Da costruire

- Uno script di creazione per settimana, così il laboratorio riparte con un comando se lo interrompi.
- Lo script di pulizia, da lanciare sempre a fine sessione.
- Un budget con avviso via email sulla subscription, impostato nella settimana 03.

Bicep e Terraform non sono materia d'esame per l'AI-200: se li usi, fallo perché ti fanno comodo,
non per il programma.

## Controllo prima di chiudere il portatile

```bash
az group list --query "[?starts_with(name, 'rg-ai200')].name" -o tsv
```

Se stampa qualcosa, stai pagando.
