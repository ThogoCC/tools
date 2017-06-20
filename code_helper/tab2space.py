#!/usr/bin/env python

import os
import os.path
import argparse

#
# @desc: convert one tab character to four space character
# @args: filename
# @returns: converted file name 
#
#
def tab_to_x(x, in_filename, out_filename=''):
    if not in_filename:
        print("input file name can't be empty")
        return ''
    if not out_filename:
        file_prefix, file_ext = os.path.splitext(in_filename)
        out_filename = file_prefix + '_out' + file_ext
    try:
        fcontent = ''
        with open(in_filename, "r+") as fin:
            fcontent = fin.read()
        content_list = fcontent.split("\t")
        with open(out_filename, "w+") as fout:
            fout.write(x.join(content_list))
    except Exception as e:
        print("failed to convert %s" % in_filename)
    return out_filename


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", nargs='+', type=str, help='input files')
    parser.add_argument("--dir", nargs='+', type=str, help='input file directory')
    parser.add_argument("--keepname", action="store_true", help='don\'t change converted file name')
    args = parser.parse_args()
    if args.file:
        for filename in args.file:
            if args.keepname:
                tab_to_x("    ", filename, filename)
            else:
                tab_to_x("    ", filename)
    if args.dir:
        for dirname in args.dir:
            files = os.listdir(dirname)
            for filename in files:
                if filename.startswith('.'):
                    continue
                full_filename = os.path.join(dirname, filename)
                if os.path.isdir(full_filename):
                    continue
                if args.keepname:
                    tab_to_x("    ", full_filename, full_filename)
                else:
                    tab_to_x("    ", full_filename)

