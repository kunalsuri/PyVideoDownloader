import os
import subprocess

# Run Streamlit script using subprocess
def run_streamlit():
    streamlit_file = "YouTube_Downloader.py"
    subprocess.Popen(["streamlit", "run", streamlit_file])

if __name__ == "__main__":
    run_streamlit()