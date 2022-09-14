touch temp.json
echo $gcp_credential > temp.json
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-402.0.0-linux-x86_64.tar.gz
export SERVICE_ACCOUNT = 'naveen-master-sa@inviz-gcp.iam.gserviceaccount.com'
export REGION= 'asia-south1'
export ENDPOINT_NAME = 'spellcheck-vertex-ai-ep'
export MODEL_NAME1 = 'spellcheck-modelv1'
export MODEL1_ID = 'spellcheck-model-id01'
# export MODEL_NAME2= 'Model_2'
# export MODEL2_ID = 'MY_Model_02'
export CONTAINER_IMAGE = 'gcr.io/inviz-gcp/spellcheck-inference-vertex-ai-demo:latest'
export PROJECT = 'inviz-gcp'
gcloud auth activate-service-account =$SERVICE_ACCOUNT --key-file=temp.json --project=$PROJECT

gcloud ai models upload --region=$REGION \
          --display-name=$MODEL_NAME1 \
          --container-image-uri=$CONTAINER_IMAGE \
          --models-id = $MODEL1_ID
          --container-predict-route=/predict
          

gcloud ai endpoints create --region=$REGION
          --display-name=$ENDPOINT_NAME

gcloud ai endpoints deploy-model --region=$REGION \
          --model=$MODEL1_ID \
          --display-name=$MODEL_NAME1 \
          --machine-type=n1-highmem-2 \
          --min-replica-count=1 \
          --max-replica-count=2 \
          --traffic-split=0=100
