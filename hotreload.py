#!/usr/bin/env python3
import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class PythonFileHandler(FileSystemEventHandler):
    def __init__(self, script_path):
        self.script_path = script_path
        self.process = None
        self.start_process()

    def start_process(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        
        print(f"\n🔄 Reloading {self.script_path}...")
        self.process = subprocess.Popen([sys.executable, self.script_path])

    def on_modified(self, event):
        if event.is_directory:
            return
        
        if event.src_path.endswith('.py'):
            print(f"📝 File changed: {event.src_path}")
            time.sleep(0.1)  # Brief delay to ensure file write is complete
            self.start_process()

if __name__ == "__main__":
    script_to_watch = "sort.py"
    
    event_handler = PythonFileHandler(script_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    print(f"🔍 Watching {script_to_watch} for changes...")
    print("Press Ctrl+C to stop")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if event_handler.process:
            event_handler.process.terminate()
        print("\n👋 Hot reload stopped")
    
    observer.join()