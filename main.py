from sys import exit
from os import listdir, makedirs, remove
from os.path import join, isfile, isdir, exists
from argparse import ArgumentParser
import subprocess

from moi_parser import read_moi_file_time

parser = ArgumentParser("python3 main.py", description="Convert moi/mod file combinations to mp4 files")
parser.add_argument("-i", "--input-directory", default=".", help="Input directory with moi/mod files")
parser.add_argument("-o", "--output-directory", default="output", help="Output directory where the mp4 files should be saved")
parser.add_argument("--ignore-existing-files", action="store_true", help="Ignore all files their mp4 files already exist")
parser.add_argument("-p", "--progress", action="store_true", help="Show progress")
parser.add_argument("-v", "--verbose", action="store_true")

def find_moi_files(directory):
    for file in listdir(directory):
        path = join(directory, file)
        if isfile(path) and file.endswith(".MOI") and exists(path.replace(".MOI", ".MOD")):
            yield path
        elif isdir(path):
            for p in find_moi_files(path):
                yield p

def check_ffmpeg():
    retcode = subprocess.call(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if retcode != 0:
        exit(f"FFMPEG check return code {retcode}")

def convert_mod_mp4(mod_filepath, mp4_filepath):
    try:
        retcode = subprocess.call(["ffmpeg", "-y", "-i", mod_filepath, "-vcodec", "libx264", "-acodec", "aac", mp4_filepath], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if retcode != 0:
            print(f"Error while converting {mod_filepath} -> {mp4_filepath}, ffmpeg return code {retcode}")
    except KeyboardInterrupt:
        remove(mp4_filepath)
        exit(0)
if __name__ == "__main__":
    args = parser.parse_args()
    check_ffmpeg()
    files = list(find_moi_files(args.input_directory))
    i = 0
    for filename in files:
        i += 1
        moi = read_moi_file_time(filename)
        source_path = filename.replace(".MOI", ".MOD")
        year_directory = join(args.output_directory, f"{moi.year:04}")
        if not exists(year_directory):
            makedirs(year_directory)
        target_path = join(year_directory, f"{moi.year:04}_{moi.month:02}_{moi.day:02}-{moi.hour:02}:{moi.minutes:02}:{moi.seconds // 1000:02}.mp4")
        if args.ignore_existing_files and exists(target_path):
            continue
        if args.verbose:
            print(source_path, "->", target_path)
        convert_mod_mp4(source_path, target_path)
        if args.progress:
            print(f"{round((i / len(files)) * 100, 2)}% ({i}/{len(files)})")
