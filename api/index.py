import sys
import os

# Add the project directory to sys.path to allow importing from nested folders
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "student-risk-dashboard", "backend"))

from main import app
