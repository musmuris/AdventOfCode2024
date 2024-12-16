@echo off

copy src\bin\day0.rs src\bin\day%1.rs
copy python\day0.py python\day%1.py
copy src\bin\inputs\day0.txt src\bin\inputs\day%1.txt
copy src\bin\inputs\day0.test1.txt src\bin\inputs\day%1.test1.txt

powershell -Command "(gc src\bin\day%1.rs) -replace 'day0', 'day%1' | Out-File -encoding ASCII src\bin\day%1.rs"
powershell -Command "(gc python\day%1.py) -replace 'day0', 'day%1' | Out-File -encoding ASCII python\day%1.py"

getinput.bat %1