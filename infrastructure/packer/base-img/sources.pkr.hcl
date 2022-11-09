source "googlecompute" "hackyeah-vm-image-base" {
  image_name   = "hackyeah-vm-image-base-${formatdate("YYYY-MM-DD-hh-mm-ss",timestamp())}"
  image_family = "hackyeah-vm-image-base"
  project_id   = var.project_id
  source_image = "debian-10-tf-2-10-0-v20220912"
  ssh_username = "appuser"
  ssh_private_key_file = "${path.root}/../common/appuser_id_rsa"
  zone         = var.zone
  disk_size    = 10
}