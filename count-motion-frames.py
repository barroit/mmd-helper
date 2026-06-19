#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later

from struct import unpack, unpack_from
from sys import argv

def next_chunk_cnt(stream):
	buf = stream.read(4)

	return unpack('<I', buf)[0]

def next_section(stream, size):
	chunks = next_chunk_cnt(stream)

	return stream.read(chunks * size)

def last_frame(section, size, off):
	last = -1

	while off < len(section):
		frame = unpack_from('<I', section, off)[0]

		if frame > last:
			last = frame

		off += size

	return last

vmd = open(argv[1], 'rb')

vmd.seek(50)

bone = next_section(vmd, 111)
last_frame_bone = last_frame(bone, 111, 15)

morph = next_section(vmd, 23)
last_frame_morph = last_frame(morph, 23, 15)

last_frame = max(last_frame_bone, last_frame_morph)

print(last_frame + 1)
