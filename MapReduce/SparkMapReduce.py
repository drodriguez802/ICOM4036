import re, os
os.environ['SPARK_WORKER_CORES']='4'
from datetime import datetime
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("Word Count").setMaster("local[4]")
sc = SparkContext(conf=conf)
start_time = datetime.now()
file = sc.textFile("ulyss12.txt")
wordCount = file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (re.sub(r"[^A-Za-z]+", '', word).lower(), 1)) \
	     .reduceByKey(lambda a, b: a + b)
wordCount = wordCount.takeOrdered(100, key=lambda x: -x[1])
total = datetime.now() - start_time
f = open("WordCount.txt", "w")
f.write("Execution time was: " + str(total)+"\n")
f.write("\n".join(map(lambda x: str(x), wordCount)))
f.close()
