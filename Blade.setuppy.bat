set str=%~dp0
echo %str%
cd /d "%str%..\Blade"
if exist "Blade.py" (goto A) else (goto B)

:A
Blade.py

:B
Blade.exe