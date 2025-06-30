@echo off
echo Starting Rust Wipe Vote Counter at %date% %time%
cd /d "C:\Users\Eli Young\discord-member-list"
python vote_counter_and_role_assigner.py
echo Vote counting completed at %date% %time%
pause 