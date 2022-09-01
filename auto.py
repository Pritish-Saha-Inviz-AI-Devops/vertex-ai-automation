import subprocess
import os
​
REGION=os.environ['region']





#CMD='gcloud auth activate-service-account qwertytestvai@pritish-vertex-ai.iam.gserviceaccount.com --key-file=temp.json --project=pritish-vertex-ai'
# authorize gcp with service account credential file and set the project 
​
#p=subprocess.Popen(CMD,stdout=subprocess.PIPE,shell=True)
​
# list the models in the vertex ai 
​
​
# endpoint creation"
​

ENDPOINT_NAME=os.environ['ENDPOINT_NAME']
MODEL1_NAME=os.environ['Model_NAME1']
MODEL1_ID=os.environ['MODEL1_ID']
CONTAINER_IMAGE=os.environ['CONTAINER_IMAGE']
PROJECT=os.environ['PROJECT']
REGION=os.environ['REGION']
MODEL2_NAME=os.environ['Model_Name2']
MODEL2_ID=os.environ['Model2_ID']













# step 1 create model
p=subprocess.Popen('gcloud ai models upload --region={}  --display-name={} --container-image-uri=gcr.io{} --model-id ={}'.format(REGION,MODEL1_NAME,IMAGE,MODEL1_ID),stdout=subprocess.PIPE, shell=True)
​
# step 2 create 2nd model
p=subprocess.Popen('gcloud ai models upload --region={}  --display-name={} --container-image-uri=gcr.io{} --model-id ={}'.format(REGION,MODEL2_NAME,IMAGE,MODEL2_ID),stdout=subprocess.PIPE, shell=True)
​

# step 3 endpoint creation


p=subprocess.Popen('gcloud ai endpoints create  --region={} --display-name={}'.format(REGION,ENDPOINT_NAME),stdout=subprocess.PIPE, shell=True)
​


'''
​
p=subprocess.Popen('gcloud ai endpoints list --region={}'.format('us-central1'),stdout=subprocess.PIPE, shell=True)
li=list(p.communicate())
li=li[0].split()
print(type(li[0]))
for i in range(len(li)):
    print(li[i])
​
​'''
# step 4 deploy model to endpoint
​
p=subprocess.Popen('  gcloud ai endpoints deploy-model {} \
  --region={} \
  --model={} \
  --display-name=$DEPLOYED_MODEL_NAME \
  --machine-type=n1-standard-4 \
  --min-replica-count=1 \
  --max-replica-count=2 \
  --traffic-split=0=100'.format(ENDPOINT_ID,REGION,MODEL1_ID))
​

# step 5 deploy other model to endpoint

p=subprocess.Popen(' gcloud ai endpoints deploy-model {} \
  --region={} \
  --model={} \
  --display-name=$DEPLOYED_MODEL_NAME \
  --machine-type=n1-standard-4 \
  --min-replica-count=1 \
  --max-replica-count=2 \
  --traffic-split=0=40, {} =60'.format(ENDPOINT_ID,REGION,MODEL2_ID,MODEL1_ID))




​
