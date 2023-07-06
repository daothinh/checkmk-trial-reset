import subprocess

def install_beautifulsoup():
    try:
        subprocess.check_call(['pip', 'install', 'beautifulsoup4'])
        print("Beautiful Soup installed successfully.")
    except subprocess.CalledProcessError:
        print("Installation failed. Please make sure pip is installed and try again.")

# Usage
install_beautifulsoup()
