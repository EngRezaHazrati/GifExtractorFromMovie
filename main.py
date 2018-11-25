import cv2
import os
import args
import imageio
import numpy
from PIL import Image

arguments = args.setup()

videoSource = arguments.video
requestedResolution = int(arguments.resolution)
if requestedResolution < 1 or requestedResolution > 3:
  raise Exception('Requested resolution is not in the acceptable range')
videoDestinationPath = arguments.out

if __name__ == '__main__':
  if videoSource == '':
    raise Exception('requested frame is longer than video.')

  if not os.path.isfile(videoSource):
    raise Exception('video not found.')

  video = cv2.VideoCapture(videoSource)

  videoLength = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) #returns the total number of frames in video
  videoFrameWidth=video.get(cv2.CAP_PROP_FRAME_WIDTH) #returns the width size of frames in video
  videoFrameHeight=video.get(cv2.CAP_PROP_FRAME_HEIGHT) #returns the height size of frames in video

  fps = int(video.get(cv2.CAP_PROP_FPS)) #returns the FPS rate of video
  videoLengthInSeconds = videoLength / fps #returns the time of the video in seconds and milliseconds

  # 1 is the prop for frame position in cv2 in python 3
  im=[]
  frameNumber=1
  outputResolution=( int(videoFrameWidth // requestedResolution) , int(videoFrameHeight // requestedResolution))
  print(outputResolution)
  frameJumpInterval = videoLength // 20
  while(frameNumber < videoLength):
    video.set(1,frameNumber)
    success, image = video.read()

    if videoDestinationPath:
      dest = os.path.abspath(videoDestinationPath)
    else:
      if not os.path.isdir('./assets/output'):
        os.mkdir(os.path.realpath(os.getcwd() + '/assets/output'))
      dest = os.path.realpath(os.getcwd() + '/assets/output')
    
    if success == False:
      video.release()
      raise Exception('failed to read the frame.')

    outputJPG_File= dest + '/frame-%d.jpg' % frameNumber
    cv2.imwrite(outputJPG_File , image)
    temp_image=Image.open(outputJPG_File, 'r')
    im.append(numpy.array(temp_image.resize(outputResolution)))
    frameNumber += frameJumpInterval
    os.remove(outputJPG_File)
    
  print(len(im))
  images=numpy.array(im)
  outputPath= dest + '/sample.gif'
  imageio.mimsave( outputPath, images, duration=0.5 )  


  del im
  del images
  video.release()