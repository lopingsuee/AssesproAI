from pathlib import Path
from moviepy import VideoFileClip

def extract_wav16k(video_path: Path, cfg) -> Path:
    outdir = Path(cfg["paths"]["tmp_audio"]); outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / (video_path.stem + ".16k.wav")
    clip = VideoFileClip(video_path.as_posix())
    clip.audio.write_audiofile(out.as_posix(), fps=16000, nbytes=2, codec="pcm_s16le", ffmpeg_params=["-ac","1"])
    clip.close()
    return out