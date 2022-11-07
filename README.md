## Infrastructure setup
### Gcloud installation
1. Create directory where you'd like to store gcloud content and go cd to it
2. Run following commands and follow installation guide
```
sudo apt install curl && \
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-408.0.1-linux-x86_64.tar.gz && \
tar -xf google-cloud-cli-408.0.1-linux-x86_64.tar.gz && \
rm google-cloud-cli-408.0.1-linux-x86_64.tar.gz && \
google-cloud-sdk/install.sh && \
google-cloud-sdk/bin/gcloud init
```
### Packer and Terraform installation
1. Run following commands
```
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg && \
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list && \
sudo apt update && sudo apt install packer && sudo apt install terraform
```
2. Run command ```gcloud auth application-default login``` and provide your Google credentials


### Usage

Replace ``<REPO_PATH>`` in command 
```
gcloud secrets versions access latest --secret=appuser-ssh-key  --format='get(payload.data)' | tr '_-' '/+' | base64 -d > <REPO_PATH>/infrastructure/packer/resources/appuser_id_rsa
```
and run it. After that you are able to run scripts:
- ``deploy.sh`` to deploy current state of your local repository to GCP
- ``destroy.sh`` to destroy everything created in GCP ()

