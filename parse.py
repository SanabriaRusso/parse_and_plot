import numpy
import pprint 

if __name__ == "__main__":
    data = {}
    filename = "data.txt"

    with open(filename) as file:
        for line in file:
            l = line.split()
            key = l[0]
        
            if key not in data.keys():
                data.setdefault(key,{})
        
            for idx,val in enumerate(l[1:]):
                if idx not in data[key].keys():
                    data[key].setdefault(idx,[])
                data[key][idx].append(val)

    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(data)

    outputFile = "data.dat"
    out = open(outputFile, 'w')
    for k,v in data.items():
    	print "-->For %s stations" % k
    	for idx,l in v.items():
    		arr = numpy.array([l]).astype(numpy.double)
    		print "\tAverage: %s" % numpy.mean(arr)
    		print "\tStandard deviation: %s" % numpy.std(arr)
    		out.write("%s %s %s\n" % (k, numpy.mean(arr), numpy.std(arr)))
