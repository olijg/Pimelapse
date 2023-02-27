#!/bin/bash

ffmpeg \
	-framerate 24 \
	-pattern_type glob -i 'timelapse/*.jpg' \
	 -vf scale=-1:720 \
	 out.gif
