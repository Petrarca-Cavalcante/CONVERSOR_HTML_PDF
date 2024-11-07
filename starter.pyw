import os, time
import subprocess
import sys

def run_main():
    # Path to the pythonw.exe in the virtual environment
    venv_python = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), "venv", "Scripts", "pythonw.exe")  
    main_script = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), "app", "interface.py")
    print("\n",venv_python, "\n\n", main_script)
    print(os.path.isfile(venv_python), os.path.isfile(main_script))

    if not os.path.exists(venv_python):
        print(f"Error: Virtual environment's pythonw.exe not found at {venv_python}.")
        sys.exit(2)

    # Path to your main.pyw script
    
    if not os.path.exists(main_script):
        print(f"Error: {main_script} not found.")
        sys.exit(2)

    # Run the main.pyw script using pythonw.exe from the venv
    try:
        subprocess.check_call([venv_python, main_script])
    except subprocess.CalledProcessError as e:
        print(f"Error running {main_script}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_main()
