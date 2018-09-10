#!/bin/bash

host=$1
service=$2
time=`date +%F-%T`
usage(){
cat<< EOF
usage: $0 (主机|组名) (服务名=cpees|CPEES|cpees2|CPEES2|webservice|WEBSERVICE|webservice2|WEBSERVICE|pcl|MESSAGE|message|PCL|BATCHFORGJSJ|batchforgjsj|BATCHFORGJSJ2|batchforgjsj2|report|REPORT|report2|REPORT2)
EOF
exit 1
}
if [ $# -lt 2 ]; then
    usage
	exit 1
fi 

echo $time

ansible -i /etc/ansible/weblogic $host -m script -a "/home/weblogic/script/service.sh $service"



