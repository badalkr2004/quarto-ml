# Publish Learn ML to Posit Connect Cloud
# Docs: https://quarto.org/docs/publishing/posit-connect-cloud.html
#
# First time:
#   1. Create a free account at https://connect.posit.cloud (sign in with GitHub/Google/etc.)
#   2. Stay logged in in your default browser
#   3. Run:  .\publish.ps1
#   4. When asked to Authorize, press Y / Enter and approve in the browser

$ErrorActionPreference = "Stop"
$quarto = Join-Path $PSScriptRoot ".tools\quarto\bin\quarto.exe"
if (-not (Test-Path $quarto)) {
  Write-Host "Quarto not found at $quarto"
  exit 1
}

Set-Location $PSScriptRoot
Write-Host "Publishing to Posit Connect Cloud..."
Write-Host "Make sure you are logged into https://connect.posit.cloud in your browser."
& $quarto publish posit-connect-cloud
