import ffmpeg
import os
import sys

input_file = "Max Gazzè - La Vita Com'è.m4a"
output_file = "Max Gazzè - La Vita Com'è.mp3"

print("Current working directory:", os.getcwd())
print("Input file:", input_file)
print("Full input path:", os.path.abspath(input_file))
print("File exists?", os.path.exists(input_file))

if not os.path.exists(input_file):
    print("❌ The input file does NOT exist. Check the name/path.")
    sys.exit(1)

try:
    stream = ffmpeg.input(input_file)
    # use native mp3 encoder instead of libmp3lame
    stream = ffmpeg.output(stream, output_file, acodec='mp3')
    out, err = ffmpeg.run(
        stream,
        overwrite_output=True,
        capture_stdout=True,
        capture_stderr=True
    )
    print("✅ Conversion finished.")
    print("Output file:", os.path.abspath(output_file))
    print("FFmpeg log:\n", err.decode("utf-8", errors="ignore"))
except ffmpeg.Error as e:
    print("❌ FFmpeg error!")
    print(e.stderr.decode("utf-8", errors="ignore"))

