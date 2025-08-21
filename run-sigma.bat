@echo off
REM Script para iniciar SIGMA en Windows (cmd)

REM Moverse a la carpeta del proyecto
cd /d G:\Mi unidad\Desarrollo\SIGMA

REM Activar el entorno virtual (.venv)
call .venv\Scripts\activate.bat

REM Definir variable de entorno para Flask
set FLASK_APP=run.py
set FLASK_ENV=development

REM Ejecutar el servidor
flask run

pause