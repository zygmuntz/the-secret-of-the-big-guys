'compute AUC from VW validation and predictions file'

import sys, csv, math
from ml_metrics import auc

test_file = sys.argv[1]
predictions_file = sys.argv[2]

test_reader = csv.reader( open( test_file ), delimiter = " " )
p_reader = csv.reader( open( predictions_file ), delimiter = "\n" )

ys = []
ps = []

for p_line in p_reader:
	test_line = test_reader.next()
	
	p = float( p_line[0] )
	p = math.tanh( p )
	ps.append( p )
	
	y = float( test_line[0] )
	ys.append( y )
	
AUC = auc( ys, ps )

#print "%s %s" % ( test_file, predictions_file )
print "AUC: %s" % ( AUC )
print "error: %s" % ( 1 - AUC )
print