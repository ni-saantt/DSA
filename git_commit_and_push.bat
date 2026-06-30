@echo off
REM Script to commit and push all changes in the DSA LAB repository
git add .
git commit -m "Refactor DSA scripts into classes and add comments"
git push
