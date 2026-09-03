#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from project_team.crew import ProjectTeam
from crewai.crew import Crew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the crew.
    """
    app = input("Enter the application name: ") or "A ECommerce Web Site that sells Gym Equipment"
    feature_count = input("Enter the number of features to generate: ") or "5"
    inputs = {
        'application': app,
        'module_name': 'Components.py',
        'current_year': str(datetime.now().year),
        'feature_count': feature_count,
    }

    os.makedirs('output/' + inputs['application'], exist_ok=True)
    
    try:
        result = ProjectTeam().crew().kickoff(inputs=inputs)
        print(f"Crew run completed successfully with result: {result}.")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()

