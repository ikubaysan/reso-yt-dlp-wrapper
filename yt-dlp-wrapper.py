# Build with pyinstaller --onefile --name=yt-dlp yt-dlp-wrapper.py
import sys
import subprocess

# Define paths
yt_dlp_path = r"C:\Program Files (x86)\Steam\steamapps\common\Resonite\RuntimeData\yt-dlp-real.exe"

# Construct command with forced argument
args = ["--cookies-from-browser", "firefox"] + sys.argv[1:]
full_command = [yt_dlp_path] + args

# Execute yt-dlp-real.exe and stream output to console
process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Stream stdout
for line in iter(process.stdout.readline, ""):
    print(line, end="")

# Stream stderr
for line in iter(process.stderr.readline, ""):
    print(line, end="")

# Close streams and wait for process to finish
process.stdout.close()
process.stderr.close()
process.wait()
