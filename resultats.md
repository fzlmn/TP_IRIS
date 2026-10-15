# Résultats

## Mesures (étapes 3 et 5)

| Image | Taille | Build à froid | Rebuild après modification |
|---|---|---|---|
| iris-train:naive | | | |
| iris-train:opt | | | |
| iris-infer:naive | | | |
| iris-infer:opt | | | |

## Trivy (étape 7)

| Image | CRITICAL | HIGH |
|---|---|---|
| iris-infer:naive | | |
| iris-infer:opt | | |

Failles critiques corrigées :
- CVE-... (bibliothèque ...) : présente dans naive, absente de opt
- CVE-... (bibliothèque ...) : présente dans naive, absente de opt