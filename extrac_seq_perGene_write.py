#!/usr/bin/python3
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help = "Input file name", type = str, dest='input', required=True)
parser.add_argument("-o", "--output", help = "Output file name", type = str, dest='output', required=True)
parser.add_argument("-k", "--kmer", help = "Kmer size", type = int, dest='kmer', required=True)
parser.add_argument("-w", "--window", help = "Window size", type = int, dest='window', required=True)

args = parser.parse_args()

input_file = args.input
output_file = args.output
kmer = args.kmer
window = args.window


for record in SeqIO.parse(input_file, "fasta"):
	chr_id = record.id
	seq = record


print(str(len(seq)))
print(chr_id)

all_string = []

seqn = "N"*kmer 

with open(output_file, "a") as output_handle:
	for start in range(1, len(seq), window):
		subseq = seq.seq[start-1:start-1+kmer]
		record = SeqRecord(subseq, '%i' %start, '', '')
		if len(record) == kmer and subseq != seqn:
			SeqIO.write(record, output_handle, "fasta")
			#all_string.append(record)

print(len(all_string))

#SeqIO.write(all_string, output_file, "fasta")

