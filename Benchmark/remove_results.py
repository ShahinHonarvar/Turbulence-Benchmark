import os
import shutil


def remove_results(model):
    for q in range(1, 61):
        parent_directory = f"Q{q}/"
        prefix = f"{model}_result"
        directories = os.listdir(parent_directory)
        matching_directories = [
            directory for directory in directories if directory.startswith(prefix)
        ]
        if matching_directories:
            for d in matching_directories:
                print(f"Results of question {q} are removed.")
                shutil.rmtree(f"Q{q}/{d}")

        if os.path.exists(parent_directory + "__pycache__") and os.path.isdir(
            parent_directory + "__pycache__"
        ):
            shutil.rmtree(parent_directory + "__pycache__")


remove_results("fake")
