import shutil
import subprocess
from pathlib import Path

output_paths = ['build', 'json_variable.egg-info', 'dist']
for output_path in output_paths:
    po = Path(output_path)
    if po.exists():
        shutil.rmtree(str(po))

subprocess.run(['python3', 'setup.py', 'sdist', 'bdist_wheel']).check_returncode()
subprocess.run(['python3', '-m', 'twine', 'upload', 'dist/*']).check_returncode()
