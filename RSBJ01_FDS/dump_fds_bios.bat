@echo off
fds_bios.py %1 temp.bin
fds_bios_patch.py temp.bin disksys.rom
del temp.bin
pause
