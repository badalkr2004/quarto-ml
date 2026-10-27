# Preview the Learn ML Quarto site
$ErrorActionPreference = "Stop"
$quarto = Join-Path $PSScriptRoot ".tools\quarto\bin\quarto.exe"
if (-not (Test-Path $quarto)) {
  Write-Host "Quarto not found at $quarto"
  Write-Host "Install from https://quarto.org/docs/get-started/ or re-extract the portable zip into .tools\quarto"
  exit 1
}
Set-Location $PSScriptRoot
& $quarto preview
