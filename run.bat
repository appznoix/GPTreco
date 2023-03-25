@echo off
cls
if "%~1"=="" goto blank

streamlit run %1.py
goto end

:blank
streamlit run Inicio.py

:end