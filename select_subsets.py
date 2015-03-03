'''
python select_subsets.py $input $output $output.id $__new_file_path__ $incl_excl $select

Uses multiple file output, see: https://wiki.galaxyproject.org/Admin/Tools/Multiple%20Output%20Files

First file in history will be $output (and it contains $name="output1" as indicated in xml <output> section.
It is up to our script to specify when to write to other subsequent files.
File name will iterate from "output2","output3",... according to suffix 
determined by "Group" column in data, which is the second-last column.
$__new_file_path__ handles subsequent output files.
$output_other_file = "primary_%s_%s_visible_tabular" % (output1.id, name)

Design Issue: Galaxy insists that first data file be written, but file name is 
already set for that file; we can't use group key in its name
- First dataset file written goes to $output file; key is ignored.
- Subsequent dataset files are written to $__new_file_path/$other_file which galaxy adds to history list.

ISSUE: This is supposed to be refreshing history using force_history_refresh="True"
 in xml <tool> tag but that doesn't seem to be working. Might just be a DNS issue?

'''

def stop_err( msg ):
    sys.stderr.write("%s\n" % msg)
    sys.exit(1)

import sys 

FORMAT_HELP = 'Did you remember to number the input dataset (last column), and provide a group flag (=1 to start a group) in second last column? '

try:
    input, output, output_id, new_file_path, incl_excl, select = sys.argv[1:]
except:
    stop_err('you must provide the arguments input, output, incl_excl and select.')
    
lines = {}
try:
    lines = dict([(int(num), '') for num in select.split(',')])
except:
    stop_err(FORMAT_HELP)

include = bool(int(incl_excl))
if include:
    print 'Including selected lines...'
else:
    print 'Excluding selected lines...'

oldGroupKey = ''
#Tried to have all datasets be known by 2nd last column text, 
#but we're supposed to fix first f_out.open() from [output] parameter?
firstFile = True

with open(input) as f_in:
	
	for line in f_in:

		cols = line.split('\t')
		try:
			num = int(cols[-1])
			#Just use first 10 characters of group key column, in case its a long string
			groupKey = cols[-2]# [:10] 
			
		except:
			stop_err(FORMAT_HELP)

		line = '\t'. join(cols[:-2]) + '\n' 
	
		writeflag=False
		if include:
			if num in lines: writeflag=True
		else:
			if not num in lines: writeflag=True
		
		if writeflag:		

			if oldGroupKey != groupKey:
				oldGroupKey = groupKey

				if firstFile:
					f_out = open(output, 'a')	
					firstFile = False			
				else:
					f_out.close()
					new_file = "primary_%s_%s_visible_tabular" % (output_id, groupKey)
					f_out = open(new_file_path + '/' + new_file, 'a')
			
			f_out.write(line)

	f_out.close()

print 'Done.'
