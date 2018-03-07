# k-mer_extraction



The script requires firstly that the raw fastq file were shuffled using velvet's shuffleSequences.pl script.
The khmer v1.1 was used.
Then loaded into a counting table using the Khmer load-into-counting.py script. 
You must create a histogram graph of the k-mers using the Khmer script abundance-dist.py.

This script can be used, depending on the number of peaks and the k-mer range the following lines were changed. In line 43 contained the lowest and highest values of the peak, if the peak number was more than one, line 13 was duplicated below and outfile1/peak1.seq changed to outfile2/peak2.seq. The code from 43 to 53 were duplicated below and the highest and lowest range changed according to peak2. 

For a full description on the use of this script please read cited paper: 


Bug reports, pull requests welcome. Contact: darren.smith@northumbria.ac.uk
