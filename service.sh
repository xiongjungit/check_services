#!/bin/bash

service_name=$1
 
usage(){
cat<< EOF
usage: $0 服务名=(cpees|CPEES)|(cpees2|CPEES2)|(webservice|WEBSERVICE)|(webservice2|WEBSERVICE2)|(pcl|PCL)|(message|MESSAGE)|(batchforgjsj|BATCHFORGJSJ)|(batchforgjsj2|BATCHFORGJSJ2)|(report|REPORT)|(report2|REPORT2)
EOF
exit 1
}

restart() {
pid1=`ps -ef|grep -v grep |grep -i cpeesDomain|grep -w -i $service_name|awk '{print $2}'`
if [[ ! ${pid1} ]]; then
    echo 检测到${service_name}未启动....
    echo 开始启动${service_name}，请等待10秒......
    umask 007
    JAVA_OPTIONS="-Ddefault.client.encoding=GBK -Dfile.encoding=GBK -Duser.language=Zh -Duser.region=CN -Djava.net.preferIPv4Stack=true"
    export JAVA_OPTIONS
    nohup /app/bea/scripts/$start_script &> /dev/null
    sleep 10
    pid2=`ps -ef|grep -v grep |grep -i cpeesDomain|grep -w -i $service_name|awk '{print $2}'`
    if [[ ${pid2} ]]; then
       echo ${service_name}启动成功
    else
       echo ${service_name}未启动成功
    fi
else
    echo 检测到${service_name}已经启动....
    echo 开始停止程序${service_name}....
    nohup /app/bea/scripts/$stop_script &> /dev/null
    echo 请等待10秒，等程序完全退出....
    sleep 10
    pid3=`ps -ef|grep -v grep |grep -i cpeesDomain|grep -w -i $service_name|awk '{print $2}'`
    sleep 3
    if [[ ${pid3} ]]; then
        echo ${service_name}程序未正常退出....
        echo 强制停止程序${service_name}
        kill -9 $pid3
        echo 开始重新启动${service_name}......
        umask 007
        JAVA_OPTIONS="-Ddefault.client.encoding=GBK -Dfile.encoding=GBK -Duser.language=Zh -Duser.region=CN -Djava.net.preferIPv4Stack=true"
        export JAVA_OPTIONS
        nohup /app/bea/scripts/$start_script &> /dev/null
        echo ${service_name}程序启动成功....
    else
        echo 开始重新启动${service_name}......
        umask 007
        JAVA_OPTIONS="-Ddefault.client.encoding=GBK -Dfile.encoding=GBK -Duser.language=Zh -Duser.region=CN -Djava.net.preferIPv4Stack=true"
        export JAVA_OPTIONS
        nohup /app/bea/scripts/$start_script &> /dev/null
        echo ${service_name}程序启动成功....
     fi
fi


}


if [ $# -lt 1 ]; then
    usage
	exit 1
fi   

case $1 in
   cpees|CPEES)
	 start_script=sc.sh
	 stop_script=sc_stop.sh
	 restart 
	 ;;
   webservice|WEBSERVICE)
	 start_script=sw.sh
	 stop_script=sw_stop.sh
	 restart 
	 ;;
   cpees2|CPEES2)
	 start_script=sc2.sh
	 stop_script=sc2_stop.sh
	 restart 
	 ;;
   webservice2|WEBSERVICE2)
	 start_script=sw2.sh
	 stop_script=sw2_stop.sh
	 restart 
	 ;;
   batchforgjsj|BATCHFORGJSJ)
	 start_script=sg.sh
	 stop_script=sg_stop.sh
	 restart 
	 ;;
   batchforgjsj2|BATCHFORGJSJ2)
	 start_script=sg2.sh
	 stop_script=sg2_stop.sh
	 restart 
	 ;;
   pcl|PCL)
	 start_script=sp.sh
	 stop_script=sp_stop.sh
	 restart 
	 ;;
   message|MESSAGE)
	 start_script=sm.sh
	 stop_script=sm_stop.sh
	 restart 
	 ;;
   report|REPORT)
	 start_script=sr.sh
	 stop_script=sr_stop.sh
	 restart 
	 ;;
   report2|REPORT2)
	 start_script=sr2.sh
	 stop_script=sr2_stop.sh
	 restart 
	 ;;
	 *)
	 usage
	 ;;
esac
	 
	 
