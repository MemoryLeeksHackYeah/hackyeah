#!/bin/bash
set -e

PACKER_DIR=infrastructure/packer
packer build $PACKER_DIR

TERRAFORM_DIR=infrastructure/terraform
terraform -chdir=$TERRAFORM_DIR init --reconfigure
terraform -chdir=$TERRAFORM_DIR apply --auto-approve
