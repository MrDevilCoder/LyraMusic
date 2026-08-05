# main.py
import sys
import runpy
import importlib

def main():
    try:
        # Try to run the module
        runpy.run_module("LyraMusic", run_name="__main__", alter_sys=True)
    except ModuleNotFoundError:
        print("Module 'LyraMusic' not found. Creating a basic app...")
        # Create a basic Flask app if module doesn't exist
        from app import app
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    except Exception as e:
        print(f"Error running module: {e}")
        # Fallback to a basic app
        from app import app
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

if __name__ == "__main__":
    main()
