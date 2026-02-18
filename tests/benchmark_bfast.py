import time
import sys
import os
import numpy as np

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from bfast import BFAST
from datasets import harvest, harvest_dates, harvest_freq

def run_benchmark():
    print("Running BFAST benchmark on harvest dataset...")
    
    start_time = time.time()
    # Run BFAST
    # Parameters taken from bfast.py's main block example
    # run_test(harvest, harvest_dates, harvest_freq, "harmonic", verbosity=0)
    
    # Run 5 iterations to get a stable average
    n_runs = 5
    times = []
    
    for i in range(n_runs):
        iter_start = time.time()
        v = BFAST(harvest, harvest_dates, harvest_freq, season="harmonic", verbosity=0)
        iter_end = time.time()
        duration = iter_end - iter_start
        times.append(duration)
        print(f"Run {i+1}: {duration:.4f} seconds")
        print(f"  n_iter: {v.n_iter}")
        print(f"  Trend breaks: {v.output.trend_breakpoints}")
        print(f"  Season breaks: {v.output.season_breakpoints}")
        
    avg_time = np.mean(times[1:]) # Exclude first run
    std_time = np.std(times[1:])
    
    print(f"\nAverage time (excluding first run): {avg_time:.4f} +/- {std_time:.4f} seconds")
    return avg_time

if __name__ == "__main__":
    run_benchmark()
