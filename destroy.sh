#!/bin/bash
set -e

TERRAFORM_DIR=infrastructure/terraform
terraform -chdir=$TERRAFORM_DIR destroy --auto-approve