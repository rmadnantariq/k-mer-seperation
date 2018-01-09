# #! /usr/bin/env python
# k-mer_extraction, this script allows the manual selection of k-mers based on their abundance and count into separate fastq files. 
# This file was designed to work in part with khmer scripts and was curated by Lauren A Cowley from a khmer script.
# The use and redistribution of this script is permitted. THE USE OF THIS SCRIPT IS AT THE RISK OF THE USERS AND IN NO EVENT SHALL THE AUTHORS OF THIS SCRIPT
# BE LIABLE FOR ANY DIRECT OR INDIRECT DAMAGES TO DATA OR EQUPMENT.
# Contact: darren.smith@northumbria.ac.uk
#
import sys
import khmer
import argparse
import os
import screed
outfile1 = open('peak1.seq', 'w')

def main():
    parser = argparse.ArgumentParser(
        description="Output k-mer abundance distribution.")

    parser.add_argument('hashname')
    parser.add_argument('seqfile')
    parser.add_argument('histout')

    args = parser.parse_args()
    hashfile = args.hashname
    seqfile = args.seqfile
    histout = args.histout

    outfp = open(histout, 'w')

    print 'hashtable from', hashfile
    ht = khmer.load_counting_hash(hashfile)

    hist = {}

    for n, record in enumerate(screed.open(seqfile)):
        if n > 0 and n % 100000 == 0:
            print '...', n

        seq = record.sequence.replace('N', 'A')
        header = record.name
        quality = record.accuracy
        med, _, _ = ht.get_median_count(seq)
        if med > 14:
            if med < 79:
                outfile1.write('@')
                outfile1.write(header)
                outfile1.write('\n')
                outfile1.write(seq)
                outfile1.write('\n')
                outfile1.write('+')
                outfile1.write('\n')
                outfile1.write(quality)
                outfile1.write('\n')
        if med > 80:
            if med < 131:
                outfile2.write('@')
                outfile2.write(header)
                outfile2.write('\n')
                outfile2.write(seq)
                outfile2.write('\n')
                outfile2.write('+')
                outfile2.write('\n')
                outfile2.write(quality)
                outfile2.write('\n')

        hist[med] = hist.get(med, 0) + 1

    maxk = max(hist.keys())

    for i in range(maxk + 1):
        outfp.write('%d %d\n' % (i, hist.get(i, 0)))
    outfp.close()

if __name__ == '__main__':
    main()
