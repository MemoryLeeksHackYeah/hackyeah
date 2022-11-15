#!/bin/bash

CLOUD_SPANNER_INSTANCE="cloud-spanner-instance"
DATABASE_NAME="cloud-spanner-db"

if [[ $1 == "create" ]]; then
  gcloud spanner instances create $CLOUD_SPANNER_INSTANCE --config=regional-europe-central2 \
      --description="Cloud Spanner Instance" --nodes=1
  gcloud spanner databases create $DATABASE_NAME --instance $CLOUD_SPANNER_INSTANCE
elif [[ $1 == "destroy" ]]; then
  gcloud spanner databases delete $DATABASE_NAME --instance $CLOUD_SPANNER_INSTANCE
  gcloud spanner instances delete $CLOUD_SPANNER_INSTANCE
else
  echo "Usage: \"$0 create\" or \"$0 destroy\""
fi
