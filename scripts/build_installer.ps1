# Build the DaHood Scripts Windows installer (placeholder)
param(
    [string]$Configuration = "Release",
    [string]$Output = "installer/out"
)

$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Force -Path $Output | Out-Null

Write-Host "Building dahood-scripts $Configuration"
python -m build --wheel --outdir $Output
Copy-Item "installer/dahood-setup.iss" $Output -ErrorAction SilentlyContinue

Write-Host "Artifacts written to $Output"