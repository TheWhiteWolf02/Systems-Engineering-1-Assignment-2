library(lattice)

read.table("output-throughput-latency/stats.csv", header=TRUE) -> csvDataFrameSource
csvDataFrame <- csvDataFrameSource

trellis.device("pdf", file="graph1.pdf", color=T, width=6.5, height=5.0)

xyplot(rate~requests, 
	data=csvDataFrame, 
	xlab="Rate", 
	ylab="Throughput", 
	type="o")

dev.off() -> null 

trellis.device("pdf", file="graph2.pdf", color=T, width=6.5, height=5.0)

xyplot(requests~(latency/50000), 
	data=csvDataFrame, 
	xlab="Throughput", 
	ylab="Time", 
	type="o")

dev.off() -> null 
