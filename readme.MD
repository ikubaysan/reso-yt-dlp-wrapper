Wrapper for yt-dlp to be used with Resonite, allowing for the use of custom options.

## Instructions

1. Go to `C:\Program Files (x86)\Steam\steamapps\common\Resonite\RuntimeData\` and rename`yt-dlp.exe` to `yt-dlp-real.exe`
2. Build this script as an executable with `pyinstaller --onefile --name=yt-dlp yt-dlp-wrapper.py` - the executable will be in the `dist` folder
3. Copy this new `yt-dlp.exe` to `C:\Program Files (x86)\Steam\steamapps\common\Resonite\RuntimeData\`