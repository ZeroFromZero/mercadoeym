@echo off
echo ========================================
echo   Smoothie Paradise - Iniciando...
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado o no está en el PATH
    echo Por favor instala Python desde https://www.python.org/
    pause
    exit /b 1
)

REM Verificar si existe el entorno virtual
if not exist "venv\" (
    echo [INFO] Creando entorno virtual...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] No se pudo crear el entorno virtual
        pause
        exit /b 1
    )
    echo [OK] Entorno virtual creado
    echo.
)

REM Activar entorno virtual
echo [INFO] Activando entorno virtual...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] No se pudo activar el entorno virtual
    pause
    exit /b 1
)

REM Instalar dependencias
echo [INFO] Instalando dependencias...
pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Algunas dependencias pueden no haberse instalado correctamente
)
echo [OK] Dependencias instaladas
echo.

REM Iniciar la aplicación
echo ========================================
echo   Iniciando Smoothie Paradise...
echo   Abre tu navegador en: http://localhost:5000
echo   Presiona Ctrl+C para detener el servidor
echo ========================================
echo.
python app.py

pause
