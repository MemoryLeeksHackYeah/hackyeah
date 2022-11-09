source "googlecompute" "hackyeah-vm-image" {
  image_name   = "hackyeah-vm-image-${formatdate("YYYY-MM-DD-hh-mm-ss",timestamp())}"
  image_family = "hackyeah-vm-image"
  project_id   = var.project_id
  source_image_family = "hackyeah-vm-image-base"
  ssh_username = "appuser"
  ssh_private_key_file = "${path.root}/../common/appuser_id_rsa"
  zone         = var.zone
  disk_size    = 10
}