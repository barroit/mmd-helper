#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later

set -e

audio=${audio:-audio.m4a}
prefix=${prefix:-.}
output=${output:-output.mp4}

framerate=${1:-30}
offset=${2:-30}

ffmpeg -start_number $offset -framerate $framerate \
       -f image2 -i $prefix/%04d -i $audio \
       -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p \
       -color_primaries bt709 -color_trc bt709 -colorspace bt709 \
       -c:a aac -b:a 320k -ar 48000 -ac 2 \
       -movflags +faststart -shortest $output
