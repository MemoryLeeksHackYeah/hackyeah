#!/bin/bash
set -e

PACKER_DIR=infrastructure/packer
if [[ $1 == "all" ]]; then
  packer build $PACKER_DIR/base-img
elif [[ $1 != "terraform" ]]; then
  packer build $PACKER_DIR/app-img
fi

TERRAFORM_DIR=infrastructure/terraform
terraform -chdir=$TERRAFORM_DIR init --reconfigure
terraform -chdir=$TERRAFORM_DIR apply --auto-approve
