# Résultats

## Mesures (étapes 3 et 5)

| Image | Taille | Build à froid | Rebuild après modification |
|---|---|---|---|
| iris-train:naive | 582 | 99 | 92 |
| iris-train:opt | 135 | 80 | 5 |
| iris-infer:naive | 582 | 82 | 84 |
| iris-infer:opt | 140 | 103 | 13 |

## Trivy (étape 7)

| Image | Paquets Debian | CRITICAL | HIGH |
|---|---|---|---|
| iris-infer:naive | 469 | 19 | 405 |
| iris-infer:opt | 87 | 0 | 44 |

Failles critiques corrigées :
- CVE-2026-44172 (MariaDB : libmariadb3, mariadb-common…, injection SQL) : présente dans naive, absente de opt
- CVE-2026-50252 (libunbound8, empoisonnement du cache DNS) : présente dans naive, absente de opt

Correction appliquée : passage de python:3.11 à python:3.12-slim. L'image slim n'installe
que 87 paquets Debian au lieu de 469 ; les bibliothèques vulnérables n'y sont plus du tout.