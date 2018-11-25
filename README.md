# GifExtractorFromMovie
a simple application written in python to export GIF file from a video

## install
First of all, you need to set up `virtualenv`
```
# create new env
virtualenv env

# activate the environment
source ./env/bin/activate

# install dependencies
pip install -r requirement.txt
```

## running
```
python main.py -h

python main.py --video <path-to-video> --resolution <1:same_size,2:half_size,3:quadrant_size> --out <output-dir>
```

example:
```
# this will make a GIF file with the same resolution of video file from video and export to the same directory as source code
python main.py --video sample.mp4 --resolution 1 --out ./
```
