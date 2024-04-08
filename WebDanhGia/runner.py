import subprocess

# List of Python scripts you want to run
scripts = ['crawl_comment.py', 'demoai.py']

for script in scripts:
    try:
        # Run the script using subprocess
        subprocess.run(['python', script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script}: {e}")
    else:
        print(f"{script} executed successfully!")