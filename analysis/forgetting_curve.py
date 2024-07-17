from datetime import datetime
import numpy as np

class ForgettingCurve:
    def __init__(self, commits):
        self.commits = [datetime.strptime(commit['commit']['author']['date'], "%Y-%m-%dT%H:%M:%SZ") for commit in commits]
        self.commits.sort()

    def calculate_curve(self):
        if len(self.commits) < 2:
            print("Not enough commits to calculate intervals")
            return [1.0]
        intervals = [(self.commits[i] - self.commits[i-1]).days for i in range(1, len(self.commits))]
        if len(intervals) == 0:
            print("No intervals calculated")
            return [1.0]
        return self._exponential_decay(intervals).tolist()
    
    def _exponential_decay(self, intervals):
        intervals = np.array(intervals)
        if intervals.size == 0:
            return np.array([1.0])
        mean_interval = intervals.mean()
        print(f"Mean interval: {mean_interval}")
        decay = np.exp(-intervals / mean_interval)
        decay = np.nan_to_num(decay, nan=0.0)  # 将 NaN 值转换为 0.0
        return decay
