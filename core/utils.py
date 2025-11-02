import time
from contextlib import contextmanager

@contextmanager
def timer(label="timer"):
    t0 = time.time()
    yield
    print(f"[{label}] {time.time()-t0:.3f}s")