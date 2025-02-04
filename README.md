# SmashBrawl_FDS

使い方 - ROM の吸い出し

1. スマブラX (RSBJ01) のパーティション 4, 6 の main.dol をそれぞれ抽出
2. dump_fds_rom.bat にドラッグ&ドロップ
3. rom.fds ができたらリネームなりして保存

使い方 - BIOS の吸い出し

1. スマブラX (RSBJ01) のパーティション 4, 6 いずれかの main.dol を抽出
2. dump_fds_bios.bat にドラッグ&ドロップ
3. disksys.rom ができたらそれをそのまま保存

main.dol の抽出方法
<details><summary>[Dolphin](https://dolphin-emu.org/) を使う方法</summary>
  
  1. 右クリックから「プロパティ」 → 「構造」タブを開く
  2. HBAJ01, HBCJ01 でそれぞれ右クリック → 「システムデータを抽出...」 をクリック
  3. sys フォルダ に main.dol がある
  
</details>
<details><summary>[WiiScrubber](https://wiidatabase.de/downloads/pc-tools/wiiscrubber/) を使う方法</summary>
  
  1. MakeKeyBin.exe を起動し, ウィンドウの指示に従い値を入力
  2. WIIScrubber.exe を起動し, 「LOAD ISO」をクリックし, RSBJ01 の ROM を選択
  3. Partition 4, 6 の main.dol を選択し, 右クリック → 「Extract」をクリック
  
</details>
