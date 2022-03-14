import os
import stat

def prepare_exp(SSHHost, SSHPort, REMOTEROOT, optpt):
    f = open("config", 'w')
    f.write("Host benchmark\n")
    f.write("   Hostname %s\n" % SSHHost)
    f.write("   Port %d\n" % SSHPort)
    f.close()
    

    f = open("run-experiment.sh", 'w')
    f.write("#!/bin/bash\n")
    f.write("set -x\n\n")
    
    f.write("ssh -o StrictHostKeyChecking=no -F config benchmark \"nohup memcached -p 11222 > memcached.out 2> memcached.err &1& echo $! > memcached.pid &\"\n") # adjust this line to properly start memcached
    
    f.write("RESULT=`ssh -F config benchmark \"pidof memcached\"`\n")

    f.write("sleep 5\n")

    f.write("if [[ -z \"${RESULT// }\" ]]; then echo \"memcached process not running\"; CODE=1; else CODE=0; fi\n")
        
    f.write("mcperf --num-calls=%d --num-conns=%d -s %s> stats.log\n\n" % (optpt["noRequests"], optpt["concurrency"], SSHHost))
   
    # add a few lines to extract the "Response rate" and "Response time \[ms\]: av and store them in $REQPERSEC and $LATENCY"
    f.write("REQPERSEC=`sed -n -e 's/^Response rate: //p' stats.log | cut -d\" \" -f1`\n")
    f.write("LATENCY=`sed -n -e 's/^Response time \\[ms\\]: avg //p' stats.log | cut -d\" \" -f1`\n")
    f.write("ssh -F config benchmark \"sudo kill -9 $(cat memcached.pid)\"\n")

    f.write("echo \"requests latency\" > stats.csv\n")
    f.write("echo \"$REQPERSEC $LATENCY\" >> stats.csv\n")
    
    f.write("scp -F config benchmark:~/memcached.* .\n")

    f.write("if [[ $(wc -l <stats.csv) -le 1 ]]; then CODE=1; fi\n\n")
    
    f.write("exit $CODE\n")

    f.close()
    
    os.chmod("run-experiment.sh", stat.S_IRWXU) 
