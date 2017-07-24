set str=%~dp0
echo %str%
set path=%str%..\Scripts\Blade\lib;%PATH%
cd /d "%str%..\Scripts\Blade\bin"
java -classpath "%str%..\Scripts\Blade\lib\*;%str%..\Scripts\Blade\bin;.;%JAVA_HOME%\lib\dt.jar" Main