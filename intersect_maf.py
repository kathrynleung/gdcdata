import os, sys, argparse

# functions
def parse_maf(fp):
	''' Return a dictionary with vars[patient][variant_set]'''
	caller_vars = {}

	fh = open(fp, 'r')
	for line in fh:
		temp = line.strip().split('\t')
		if line[0] == '#' or temp[0] == 'Hugo_Symbol':
			continue
		ID = temp[16] + '_' + temp[17] # 'tumor'_'normal'
		if ID not in caller_vars:
			caller_vars[ID] = set()
		chrom =temp[4]
		s_pos = temp[5]
		e_pos = temp[6]
		ref = temp[11]
		tum_allele_1 = temp[12]
		tum_allele_2 = temp[13]
		var = (chrom, s_pos, e_pos, ref, tum_allele_1, tum_allele_2)
		caller_vars[ID].add(var)

	return(caller_vars)


def two_set(dat_1, dat_2):
	''' have to compare each patient's calls'''
	
	inter_all = 0
	diff_1_all = 0
	diff_2_all = 0

	# intersect patient keys
	patients = set(list(dat_1.keys())) & set(list(dat_2.keys()))

	for patient in patients:
		set_1 = dat_1[patient]
		set_2 = dat_2[patient]
		inter = len(set_1 & set_2)
		diff_1 = len(set_1 - set_2)
		diff_2 = len(set_2 - set_1)

		inter_all = inter_all + inter
		diff_1_all = diff_1_all + diff_1
		diff_2_all = diff_2_all + diff_2

	return(len(patients), inter_all, diff_1_all, diff_2_all)


def four_set(dat_1, dat_2, dat_3, dat_4):
	''' have to compare each patient's calls'''
	
	inter_all = 0
	diff_1_all = 0
	diff_2_all = 0

	# intersect patient keys
	patients = set(list(dat_1.keys())) & set(list(dat_2.keys())) & set(list(dat_3.keys())) & set(list(dat_4.keys()))

	for patient in patients:
		set_1 = dat_1[patient]
		set_2 = dat_2[patient]
		inter = len(set_1 & set_2)
		diff_1 = len(set_1 - set_2)
		diff_2 = len(set_2 - set_1)

		inter_all = inter_all + inter
		diff_1_all = diff_1_all + diff_1
		diff_2_all = diff_2_all + diff_2

	return(len(patients), inter_all, diff_1_all, diff_2_all)

"""
def set_operations(*args):
	'''Takes multiple sets and performs all set operations.'''

	union = 

	final_list = list(set().union(lst1, lst2, lst3)) # can this input be a list of sets?
"""

# main
possible_callers = ('mutect', 'muse', 'somaticsniper', 'varscan')
possible_cancers = ('ACC','BLCA','BRCA','CESC','CHOL','COAD','DLBC','ESCA','GBM','HNSC', \
					'KICH','KIRC','KIRP','LAML','LGG','LIHC','LUAD','LUSC','MESO','OV',\
					'PAAD','PCPG','PRAD','READ','SARC','SKCM','STAD','TGCT','THCA','THYM',\
					'UCEC','UCS','UVM')

parser = argparse.ArgumentParser(description='Intersect variants per cancer type.')
parser.add_argument('--callers', nargs='+', action='store', dest='callers', default=possible_callers, help='Provide(s) of caller')
parser.add_argument('--cancer', action='store', dest='cancer', type=str, help='Provide TCGA caner type', required=True)
args = parser.parse_args()

# must be a valid caller

# must be a valid cancer
if args.cancer not in possible_cancers:
	raise Exception('The provided cancer is not a TCGA cancer type.')

for caller in args.callers:
	if caller not in possible_callers:
		raise Exception('The provided caller is not valid. Please provide mutect, muse, somaticsniper, or varscan.') 

os.chdir(args.cancer)
mafs = os.listdir()

maf_fps = {}
for caller in args.callers:
	for maf in mafs:
		if caller in maf: # str in the filepath
			maf_fps[caller] = maf

print(args.callers)
print(maf_fps)

if len(maf_fps) != len(args.callers):
	raise Exception('Could not map all callers to a maf file.')

# parse maf for each caller
all_variants = {}
for caller in maf_fps:
	all_variants[caller] = parse_maf(maf_fps[caller])

# Do all pairwise
num_callers = len(args.callers)
for i in range(0, num_callers):
	if i == num_callers:
		break
	for j in range(i + 1, num_callers):
		# do pairwise
		set_vals = two_set(all_variants[args.callers[i]], all_variants[args.callers[j]])
		print(args.callers[i], args.callers[j])
		print(set_vals)




