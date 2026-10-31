# Script de Arranque Rápido en 1 Clic para TalentUP™ (Windows PowerShell)
Write-Host "================================================================" -ForegroundColor Red
Write-Host "  TALENTUP™ — PRIMERA EMPRESA AUTÓNOMA LIQUID-SOLID (v4.0)      " -ForegroundColor White
Write-Host "================================================================" -ForegroundColor Red

$backendDir = Join-Path $PSScriptRoot "02_ENGINEERING\backend"
Start-Process "http://127.0.0.1:8088"
python -m uvicorn main:app --app-dir $backendDir --host 127.0.0.1 --port 8088
