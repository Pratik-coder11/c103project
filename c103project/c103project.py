import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\coding python\c102"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event): 
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event): 
        print(f"Oops! Someone deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"Directory modified: {event.src_path}")

    def on_moved(self, event):
        print(f"Directory moved/renamed: {event.src_path} to {event.dest_path}")
        
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_system_events_tracker.py <path_to_track>")
        sys.exit(1)

    from_dir = sys.argv[1]

    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=from_dir, recursive=True)
    observer.start()

    print(f"Watching directory: {from_dir}")
    print("Press any key to stop the observer.")

    try:
        while True:
            time.sleep(2)
            print("running...")
    except KeyboardInterrupt:
        print("stopped!")
        observer.stop()

