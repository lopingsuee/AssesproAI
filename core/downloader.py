from pathlib import Path
import os, requests

def _download_direct(url: str, outpath: Path):
    outpath.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(outpath, "wb") as f:
            for c in r.iter_content(chunk_size=1<<20):
                if c: f.write(c)
    return outpath

def _download_ytdlp(url: str, outdir: Path) -> Path:
    import yt_dlp
    outdir.mkdir(parents=True, exist_ok=True)
    outtpl = str(outdir / "%(title).80s_%(id)s.%(ext)s")
    ydl_opts = {"quiet": True, "outtmpl": outtpl, "format":"mp4+bestaudio/best","merge_output_format":"mp4","noplaylist":True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        path = ydl.prepare_filename(info)
    base = os.path.splitext(path)[0] + ".mp4"
    return Path(base if os.path.exists(base) else path)

def fetch_video_to_local(url: str, cfg) -> Path:
    u = url.lower()
    outdir = Path(cfg["paths"]["tmp_videos"])
    if any(k in u for k in ["youtube.com","youtu.be","tiktok.com","x.com"]):
        return _download_ytdlp(url, outdir)
    if "dropbox.com" in u and "?dl=0" in url:
        url = url.replace("?dl=0","?dl=1")
    return _download_direct(url, outdir / "remote_video.mp4")