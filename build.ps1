# build.ps1

$envName = ".venv"
$packageDir = "package"
$zipName = "bot.zip"

Write-Host "Cleaning up previous build..."
if (Test-Path $packageDir) { Remove-Item $packageDir -Recurse -Force }
if (Test-Path $zipName) { Remove-Item $zipName -Force }

if (-not (Test-Path $envName)) {
    Write-Host "Creating virtual environment..."
    python -m venv $envName
}

Write-Host "Activating virtual environment..."
& "$envName\Scripts\Activate.ps1"

Write-Host "Upgrading pip..."
pip install --upgrade pip

Write-Host "Installing dependencies into package directory..."
python -m pip install -r requirements.txt -t $packageDir

Write-Host "Copying main.py to package..."
Copy-Item -Path "main.py" -Destination $packageDir

Write-Host "Creating deployment zip file..."
Compress-Archive -Path "$packageDir\*" -DestinationPath $zipName

Write-Host "Build completed. '$zipName' is ready for deployment."
