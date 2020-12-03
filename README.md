# k-mer_extraction



The script requires firstly that the raw fastq file were shuffled using velvet's shuffleSequences.pl script.
The khmer v1.1 was used.
Then loaded into a counting table using the Khmer load-into-counting.py script. 
You must create a histogram graph of the k-mers using the Khmer script abundance-dist.py. The out.hist file must be graphed and the y axis log  tansformed. You determine the count values fromt he x axis and omit the low erronous k-mers.

This script can be used, depending on the number of peaks and the k-mer range the following lines were changed. In line 43 contained the lowest and highest values of the peak, if the peak number was more than one, line 13 was duplicated below and outfile1/peak1.seq changed to outfile2/peak2.seq. The code from 43 to 53 were duplicated below and the highest and lowest range changed according to peak2. 

For a full description on the use of this script please read cited paper:  Tariq MA, Everest FLC, Cowley LA, Wright R, Holt GS, Ingram H, Duignan LAM, Nelson A, Lanyon CV, Perry A, Perry JD, Bourke S, Brockhurst MA, Bridge SH, De Soyza A, Smith DL. 2019. Temperate bacteriophages from chronic Pseudomonas aeruginosa lung infections show disease-specific changes in host range and modulate antimicrobial susceptibility. mSystems 4:e00191-18. https://doi.org/10.1128/mSystems.00191-18.

Bug reports, pull requests welcome. Contact: darren.smith@northumbria.ac.uk
