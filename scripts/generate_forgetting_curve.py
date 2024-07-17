import os
import sys
import subprocess

# Dynamically add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from my_leetcode_tracker.curve_generator import generate_forgetting_curve

# Define the root directory where your LeetCode problems are stored
root_dir = './Leetcode'

# Exclude certain directories and files
exclude_dirs = {'.github', 'scripts', 'src', '.git'}
exclude_files = {'.gitignore', 'README.md'}

# Function to clone the repository
def clone_repository(repo_url, clone_dir):
    if os.path.exists(clone_dir):
        # If the directory exists, remove it first
        subprocess.run(['rm', '-rf', clone_dir])
    subprocess.run(['git', 'clone', repo_url, clone_dir])

# Collect all directories containing LeetCode problems
problems_dirs = []

def collect_problem_dirs():
    for root, dirs, files in os.walk(root_dir):
        # Filter out the directories and files to exclude
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        files = [f for f in files if f not in exclude_files]
        
        # Add directory if it contains any files
        if files:
            problems_dirs.append(root)

if __name__ == "__main__":
    # Clone the repository
    repo_url = 'https://github.com/QingzeHu/Leetcode.git'
    clone_repository(repo_url, root_dir)
    
    # Collect problem directories
    collect_problem_dirs()
    
    # Generate forgetting curve
    generate_forgetting_curve(problems_dirs)
