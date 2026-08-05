# main.py
import sys
import os
import runpy

def main():
    try:
        # Try to run the module
        runpy.run_module("LyraMusic", run_name="__main__", alter_sys=True)
    except ModuleNotFoundError:
        print("Module 'LyraMusic' not found. Creating a basic app...")
        try:
            from app import app
            app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
        except ImportError:
            print("Error: 'app' module not found. Please create a Flask app.")
            sys.exit(1)
    except Exception as e:
        print(f"Error running module: {e}")
        try:
            from app import app
            app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
        except ImportError:
            print("Error: 'app' module not found. Please create a Flask app.")
            sys.exit(1)

if __name__ == "__main__":
    main()
