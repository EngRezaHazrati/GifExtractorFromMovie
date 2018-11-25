import argparse

def setup():
  parser = argparse.ArgumentParser(description='export jpeg frame out of mp4 video.',formatter_class=argparse.RawTextHelpFormatter)

  parser.add_argument('--video', help='source of video', required=True)
  parser.add_argument('--resolution',help='Specify the resolution of the output GIF file depends on the resolution of input file\n1:same size\n2:half size\n3:Quadrant size', required=True)
  parser.add_argument('--out', help='export destination directory')

  return parser.parse_args()