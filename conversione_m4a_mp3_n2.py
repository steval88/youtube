import ffmpeg
import os
import sys

input_file = "Pearl Jam - Thumbing My Way (Live at Chop Suey).m4a"
output_file = "Pearl Jam - Thumbing My Way (Live at Chop Suey).mp3"

print("Current working directory:", os.getcwd())
print("Input file:", input_file)
print("Full input path:", os.path.abspath(input_file))
print("File exists?", os.path.exists(input_file))

if not os.path.exists(input_file):
    print("❌ The input file does NOT exist. Check the name/path.")
    sys.exit(1)

try:
    inp = ffmpeg.input(input_file)

    # Force stereo downmix (5.1 -> 2.0) so mp3_mf can encode it
    stream = ffmpeg.output(
        inp,
        output_file,
        acodec="mp3",
        ac=2,
        audio_bitrate="192k",   # optional but sensible
        ar=44100                # optional (keep 44.1kHz)
    )

    # Helpful for debugging: see the exact ffmpeg command
    print("FFmpeg command:", " ".join(ffmpeg.compile(stream)))

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
