from flask import render_template, jsonify, current_app as app
from data.github_api import GitHubAPI
from analysis.forgetting_curve import ForgettingCurve
import os
import json
import numpy as np

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    try:
        repo = "QingzeHu/Leetcode"
        token = os.getenv('GITHUB_TOKEN')
        github = GitHubAPI(repo, token)

        files = github.get_files()
        curves = {}

        for file in files:
            if file['name'].endswith('.go'):
                commits = github.get_commits(file['path'])
                forgetting_curve = ForgettingCurve(commits)
                curve = forgetting_curve.calculate_curve()
                # 确保只有在对象是 NumPy 数组时才调用 tolist 方法
                if isinstance(curve, np.ndarray):
                    curve = curve.tolist()
                curves[file['name']] = curve

        return jsonify(curves)
    except Exception as e:
        app.logger.error(f"Error while fetching data: {e}")
        return jsonify({"error": str(e)}), 500
