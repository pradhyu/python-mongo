# How tos? 

## install using helm chart
```bash

# https://github.com/bitnami/charts/tree/master/bitnami/mongodb/#installing-the-chart
# architecture="standalone"
# architecture="replicaset"
helm uninstall my-mongo
helm upgrade --install my-mongo bitnami/mongodb \
    --set architecture=replicaset \
    --set replicaCount=4

helm uninstall my-mongo
helm install my-mongo \
    --set auth.rootPassword=secretpassword,auth.username=my-user,auth.password=my-password,auth.database=my-database \
    bitnami/mongodb

centos@ubuntu:~$ mongo --host 127.0.0.1 --authenticationDatabase my-database -u my-user -p my-password --nodb
MongoDB shell version v4.0.24
> 

# port foward the service
kubectl port-forward svc/my-mongo-mongodb-headless 27017:27017
Forwarding from 127.0.0.1:27017 -> 27017
Forwarding from [::1]:27017 -> 27017

```


## python library 

```bash
pip3 install -r requirements.txt

```
