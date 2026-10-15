# Meme role que benchmark.sh de la correction :
# taille de l'image, build a froid, rebuild apres modification du code
param(
    [string]$Image      = "iris-train:naive",
    [string]$Dockerfile = "Dockerfile.train.naive",
    [string]$Fichier    = "train.py"
)

if (-not (Test-Path $Dockerfile)) { Write-Host "Dockerfile introuvable : $Dockerfile"; exit 1 }
if (-not (Test-Path $Fichier))    { Write-Host "$Fichier introuvable"; exit 1 }

$nom = $Image -replace ':', '-'
Copy-Item $Fichier "$Fichier.bak"

try {
    Write-Host "Build a froid..."
    $debut = Get-Date
    cmd /c "docker build --no-cache -f $Dockerfile -t $Image . > build_froid_$nom.log 2>&1"
    if ($LASTEXITCODE -ne 0) { Write-Host "Echec, voir build_froid_$nom.log"; exit 1 }
    $froid = [math]::Round(((Get-Date) - $debut).TotalSeconds)

    Write-Host "Rebuild apres modification..."
    Add-Content $Fichier "# modification benchmark"
    $debut = Get-Date
    cmd /c "docker build -f $Dockerfile -t $Image . > build_chaud_$nom.log 2>&1"
    if ($LASTEXITCODE -ne 0) { Write-Host "Echec, voir build_chaud_$nom.log"; exit 1 }
    $chaud = [math]::Round(((Get-Date) - $debut).TotalSeconds)
}
finally {
    Move-Item -Force "$Fichier.bak" $Fichier
}

$taille = docker image inspect $Image --format '{{.Size}}'
$tailleMo = [math]::Round([double]$taille / 1000000)

Write-Host ""
Write-Host "Image : $Image"
Write-Host "Taille : $tailleMo Mo"
Write-Host "Build a froid : $froid s"
Write-Host "Rebuild a chaud : $chaud s"