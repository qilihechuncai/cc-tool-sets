#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

"""
ts-truncater.py is used to truncate ts stream
"""

_DEBUG = True

def help():
	s = "USAGE:\tts-truncater -i input file -l header length -o output file\n\n"
	s += "    input file:        the ts file with private header.\n"
	s += "    header length:     Default is 42\n"
	s += "    output file:       Default is output.ts\n"

	sys.stdout.write(s)

def help_and_die():
	help()
	sys.exit(0)

def truncate(input_file, length, output_file):
	fi = open(input_file, "rb")
	fo = open(output_file, "wb+")

	try:
		ts = fi.read()
		ts = ts.encode('hex')

		pattern = re.compile(r'351301.{78}')
		ts, count = re.subn(pattern, '', ts)
		ts = ts.decode('hex')
		fo.write(ts)

	finally:
		fi.close()
		fo.close()


def get_opt(name):
	try:
		index = sys.argv.index(name)
	except:
		return None

	if index >= len(sys.argv) - 1:
		return None
	return sys.argv[index + 1]

def get_opts():
	input_file = get_opt("-i")
	if not input_file:
		print("Please input the file which need to be truncated\n")
		print("You can use the --help\n")
		return None

	length = get_opt("-l")
	if not length:
		length = 42
	else:
		length = int(length)

	output_file = get_opt("-o")
	if not output_file:
		output_file = "output.ts"
	else:
		output_file = str(output_file)

	return input_file, length, output_file



def main():
	if _DEBUG == True:
		import pdb
		pdb.set_trace()
	input_file, length, output_file = get_opts()
	truncate(input_file, length, output_file)


if __name__ == "__main__":
	if "--help" in sys.argv:
		help_and_die()
	main()
