import numpy as np
import matplotlib.pyplot as plt
import os
import glob
#import plotly.plotly as py

throughput=[]
time=[]
total_throughput=[]
latency=[]
total_latency=[]
percentile_90=[]

directory="/home/gwthamy/Software/wso2sp-4.0.0-SNAPSHOT/samples/sample-clients/tcp-server/tcp-client-results"

filepath=max(glob.iglob("/home/gwthamy/Software/wso2sp-4.0.0-SNAPSHOT/samples/sample-clients/tcp-server/tcp-client-results/*.csv"), key=os.path.getmtime)
#filepath="/home/gwthamy/Software/wso2sp-4.0.0-SNAPSHOT/samples/sample-clients/tcp-server/tcp-client-results/output-54-1505302223953.csv"
# loop through each csv file in the specific folder
def get_all_files(directory):
    dir_list = os.listdir(directory)
    csv_files = []
    for e in dir_list:
        if e.endswith('.csv'):
            csv_files.append(e)
    return len(csv_files)

def file_read(filepath,start,end):
	testFile=open(filepath,'r')
	#for i in range():
	#testFile.next()
	
	content=testFile.readlines()[start:end]


	for line in content:
		line=line.strip()
		data=line.split(",")[1]
		data2=line.split(",")[5]
		data3=line.split(",")[2]
		latency_data=line.split(",")[6]
		total_latency_data=line.split(",")[7]
		percentile90=line.split(",")[3]
		
		float_throughput_data = float(data)
		thousands_throughput=float_throughput_data/1000
		float_id=float(data2)
		throughput.append(thousands_throughput)
		time.append(float_id)
		total_throughput_values=float(data3)/1000
		total_throughput.append(total_throughput_values)
		float_latency=float(latency_data)
		latency.append(float_latency)
		float_total_latency=float(total_latency_data)
		total_latency.append(float_total_latency)
		float_percentile90=float(percentile90)/1000
		percentile_90.append(float_percentile90)


length=len(throughput)
#String=str(length)

print length


throughput_image_dir=("/home/gwthamy/Software/wso2sp-4.0.0-SNAPSHOT/samples/sample-clients/tcp-server/outputGraphs/throughput_graph/output-.{}.png".format(get_all_files(directory)-1))
latency_image_dir=("/home/gwthamy/Software/wso2sp-4.0.0-SNAPSHOT/samples/sample-clients/tcp-server/outputGraphs/latency_Graph/output-.{}.png".format(get_all_files(directory)-1))

def drawChart(start,end):

	file_read(filepath,start,end)	

	#Chart for throughput	

	line = plt.figure(1,figsize=(20.0, 15.0))

	#np.random.seed(5)
	N=len(throughput)
	print N

	plt.title("Stream Processor-TCP-Throughput-Simple passthrough")

	for x in time:
		print x

	x=np.array([time])
	y=np.array([throughput])
	z=np.array([total_throughput])
	a=np.array([percentile_90])


	plt.ylabel("Throughput(thousands events/second)");
	plt.xlabel("Total elapsed time(s)");
	

	plt.plot(time,throughput, label=' Throughput in this window')

	plt.plot(x, y, "o",color='blue')
	plt.plot(time,total_throughput,color='red', label=' Entire throughput for the run')
	plt.plot(x,z,"x",color='red')
	plt.plot(time,percentile_90,color='green',label='90th percentile for throughput in this window')
	plt.plot(x,a,"*",color='green')
	plt.legend()

	#plt.show()
	
	plt.savefig(throughput_image_dir);
	plt.show()

	#chart for latency
	

	plt.figure(2,figsize=(20.0, 15.0))
	plt.title("Stream Processor-TCP-Latency-Simple passthrough")

	lat=np.array([latency])
	evt=np.array([time])
	tot_lat=np.array([total_latency])
	
	plt.ylabel("Average latency per event in this window(ms)");
	plt.xlabel(" Total elapsed time(s)");


	plt.plot(time,latency, label=' latency in this window',color='blue')

	plt.plot(x, lat, "o",color='blue')
	plt.plot(time,total_latency,color='red', label=' Entire latency for the run')
	plt.plot(x,tot_lat,"x",color='red')

	plt.legend()

	#plt.show()

	plt.savefig(latency_image_dir);
	plt.show()


drawChart(2,101)

