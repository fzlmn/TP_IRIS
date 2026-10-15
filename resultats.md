# Résultats

## Mesures (étapes 3 et 5)

| Image | Taille | Build à froid | Rebuild après modification |
|---|---|---|---|
| iris-train:naive | 582 | 99 | 92 |
| iris-train:opt | 135 | 80 | 5 |
| iris-infer:naive | 582 | 82 | 84 |
| iris-infer:opt | 140 | 103 | 13 |

## Trivy (étape 7)

| Image | CRITICAL | HIGH |
|---|---|---|
| iris-infer:naive | | |
| iris-infer:opt | | |

Failles critiques corrigées :
- CVE-... (bibliothèque ...) : présente dans naive, absente de opt
- CVE-... (bibliothèque ...) : présente dans naive, absente de opt