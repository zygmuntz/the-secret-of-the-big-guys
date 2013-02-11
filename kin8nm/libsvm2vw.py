import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

i = open( input_file )
o = open( output_file, 'wb' )

for line in i:
	line = line.replace( ' ', ' |m ', 1 )
	o.write( line )