'compute RMSE from VW validation and predictions file'

import sys, csv, math

test_file = sys.argv[1]
predictions_file = sys.argv[2]

test_reader = csv.reader( open( test_file ), delimiter = " " )
p_reader = csv.reader( open( predictions_file ), delimiter = "\n" )

squared_diffs = []
n = 0

for p_line in p_reader:
	test_line = test_reader.next()
	n += 1
	
	p = float( p_line[0] )
	y = float( test_line[0] )
	#print "%s / %s" % ( y, p )
	
	squared_diff = math.pow( y - p, 2 )
	squared_diffs.append( squared_diff )

squared_diffs = sum( squared_diffs )
MSE = squared_diffs / n
RMSE = math.sqrt( MSE )

#print "%s %s" % ( test_file, predictions_file )
print "RMSE: %s" % ( RMSE )
print