import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

cmd_commands = [
    "python -m venv venv",                    
    "call venv\\Scripts\\activate && "        
    "pip install -r requirements.txt && "     
    "deactivate"                               
]

cmd_command = " & ".join(cmd_commands)

subprocess.run(['cmd', '/C', cmd_command], cwd=script_dir, shell=True)
