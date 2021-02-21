# Picture organization scripts

Miscellaneous tools for image organization

## Video to image

Simple video to image directly in good quality:
`ffmpeg.exe -i file.mp4 -r 1 -q:v 1 output%03d.jpg`

## Tools

- `copy_except_raw.py`: Copies all files below a source folder recursively to a target folder except RAW files
- `sort_to_folders.py`: Moves jpg images in a source folder to a target folder, where they are sorted into folders by date (e.g., starting with `2019_04_12`)
- `image_extract.py`: extract a single image from a video into python
