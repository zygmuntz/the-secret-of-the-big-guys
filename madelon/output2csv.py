import os, re, csv

# regular expressions for capturing the interesting quantities
centers_pattern = '^centers: (\d+)$'
selected_centers_pattern = '^rbf param: ([0-9.]+)$'		# misleading name!
res_pattern = '^error: +([0-9.]+$)'

search_dir = "output"
results_file = '../results.csv'

os.chdir( search_dir )
files = filter( os.path.isfile, os.listdir( '.' ))
#files = [ os.path.join( search_dir, f ) for f in files ] # add path to each file
files.sort( key=lambda x: os.path.getmtime( x ))

results = []

for file in files:
	f = open( file )
	contents = f.read()
	
	# centers
	matches = re.search( centers_pattern, contents, re.M )
	try:
		centers = matches.group( 1 )
	except AttributeError:
		print "centers error 1: %s" % ( contents )
		continue
		
	# selected centers
	matches = re.search( selected_centers_pattern, contents, re.M )
	try:
		selected_centers = matches.group( 1 )
	except AttributeError:
		print "selected error 1: %s" % ( contents )
		continue		
	
	# rmse
	matches = re.search( res_pattern, contents, re.M )
	try:
		res = matches.group( 1 )
	except AttributeError:
		print "matches error 2: %s" % ( contents )
		continue
		
	results.append(( res, centers, selected_centers ))
	
writer = csv.writer( open( results_file, 'wb' ))
for result in results:
	writer.writerow( result )