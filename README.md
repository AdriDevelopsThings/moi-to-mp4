# moi-to-mp4
Convert a directory with MOI/MOD file combinations to a sorted list of mp4 files

## Run
You just need `python3.6` and `ffmpeg`.

```
usage: python3 main.py [-h] [-s SOURCE_DIRECTORY] [-o OUTPUT_DIRECTORY] [-v]

Convert moi/mod file combinations to mp4 files

options:
  -h, --help            show this help message and exit
  -s SOURCE_DIRECTORY, --source-directory SOURCE_DIRECTORY
                        Source directory with moi/mod files
  -o OUTPUT_DIRECTORY, --output-directory OUTPUT_DIRECTORY
                        Output directory where the mp4 files should be saved
  -v, --verbose
```