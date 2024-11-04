"""Copy the current repo to the students repos."""

import os
import shutil

dest = [
    "/Volumes/GitHub/_fundamentos/PRE_01_hola_mundo/",
    "/Volumes/GitHub/_descriptiva/PRE_01_hola_mundo/",
    "/Volumes/GitHub/_predictiva/PRE_01_hola_mundo/",
]


# Create a copy of the current tree directory (including all the files)
# to the dest directories. If a file begins with "_" or ".", # it will
# be ignored. if a directory begins with "_" or ".", the directory and
# all of its content will be ignored. Hidden folderes used by pytest or
# mypy, for example, will be ignored as well.

for d in dest:
    for root, dirs, files in os.walk(".", topdown=True):

        dirs[:] = [d for d in dirs if not d.startswith(".")]
        dirs[:] = [d for d in dirs if not d.startswith("_solution")]
        dirs[:] = [d for d in dirs if not d.endswith("_cache")]
        dirs[:] = [d for d in dirs if not d.endswith(".egg-info")]

        for f in files:
            if f.startswith("_copy_repo"):
                continue

            src_file = os.path.join(root, f)
            dest_file = os.path.join(d, src_file)
            dest_dir = os.path.dirname(dest_file)

            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            shutil.copy2(src_file, dest_file)

    print(f"Files copied to {d}")

print("Done!")
