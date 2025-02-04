# SmashBrawl_FDS

あらかじめ [Python 2.6](https://www.python.org/download/releases/2.6/) をインストールしてください

### 使い方 - ROM の吸い出し

1. スマブラX (RSBJ01) のパーティション 4, 6 の main.dol をそれぞれ抽出
2. dump_fds_rom.bat にドラッグ&ドロップ
3. rom.fds ができたらリネームなりして保存

### 使い方 - BIOS の吸い出し

1. スマブラX (RSBJ01) のパーティション 4, 6 いずれかの main.dol を抽出
2. dump_fds_bios.bat にドラッグ&ドロップ
3. disksys.rom ができたらそれをそのまま保存

### main.dol の抽出方法
<details><summary>Dolphin を使う方法</summary>

  1. [Dolphin](https://dolphin-emu.org/) をインストール
  2. 右クリックから「プロパティ」 → 「構造」タブを開く
  3. HBAJ01, HBCJ01 でそれぞれ右クリック → 「システムデータを抽出...」 をクリック
  4. sys フォルダ に main.dol がある
  
</details>
<details><summary>WiiScrubber を使う方法</summary>

  1. [WiiScrubber](https://wiidatabase.de/downloads/pc-tools/wiiscrubber/) をインストール
  2. MakeKeyBin.exe を起動し, ウィンドウの指示に従い値を入力
  3. WIIScrubber.exe を起動し, 「LOAD ISO」をクリックし, スマブラX (RSBJ01) の ROM を選択
  4. Partition 4, 6 の main.dol を選択し, 右クリック → 「Extract」をクリック
  
</details>
