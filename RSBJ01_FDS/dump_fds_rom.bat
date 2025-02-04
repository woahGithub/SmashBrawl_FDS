@echo off
fds_rom.py %1

mgd1cnv output_1.bin 1st_a.bin
mgd1cnv output_2.bin 1st_b.bin

del output_1.bin
del output_2.bin

fds_rom_patch.py rom.fds 1st_a.bin 1st_b.bin

del 1st_a.bin
del 1st_b.bin

pause