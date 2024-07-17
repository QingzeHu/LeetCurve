import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from .utils import parse_problem_filename

def generate_forgetting_curve(problems_dirs):
    problem_stats = {}

    for problems_dir in problems_dirs:
        for root, dirs, files in os.walk(problems_dir):
            for file in files:
                problem_number, problem_name = parse_problem_filename(file)
                file_path = os.path.join(root, file)
                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))

                if problem_number not in problem_stats:
                    problem_stats[problem_number] = {'name': problem_name, 'attempts': []}
                problem_stats[problem_number]['attempts'].append(file_mtime)

    # Ensure the forgetting_curves directory exists
    output_dir = './forgetting_curves'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate a combined forgetting curve
    plt.figure(figsize=(15, 10))

    for problem_number, stats in problem_stats.items():
        attempts = sorted(stats['attempts'])
        intervals = [(attempts[i] - attempts[i - 1]).days for i in range(1, len(attempts))]
        
        # Plot each problem's forgetting curve on the same figure
        plt.plot(intervals, marker='o', label=f'{problem_number}: {stats["name"]}')

    plt.title('Forgetting Curves for All Problems')
    plt.xlabel('Attempt Number')
    plt.ylabel('Days Since Last Attempt')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig(f'{output_dir}/combined_forgetting_curve.png')
    plt.close()
