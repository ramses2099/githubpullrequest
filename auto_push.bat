@echo off

if "%~1"=="" (
    echo Usage: auto_push.bat "branch-name" "Commit message"
    exit /b 1 
)

set "BRANCH=%~1"
set "TITLE=%~2"

if "%TITLE%"=="" (
    echo Commit message is required.
    exit /b 1 
)

echo Pull
git pull

echo Checking the status...
git status

echo Adding the changes...
git add .

echo Commiting...
git commit -m "%TITLE%"

echo Pushing branch...
git push

echo Done!