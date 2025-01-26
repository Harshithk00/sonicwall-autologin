#save this to shell:startup(win+r)
@echo off

REM Run Python script
"python-path" "your-script-path"

REM Optional: Error handling
if %errorlevel% neq 0 (
    echo Error running Sonic login script
    pause
)