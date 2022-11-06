data "google_compute_image" "hackyeah_vm_image" {
  family  = "hackyeah-vm-image"
  project = var.project_id
}

resource "google_compute_instance_template" "instance_template" {
  name_prefix             = "hackyeah-instance-template-"
  machine_type            = var.machine_type
  project                 = var.project_id
  metadata_startup_script = file("startup-script.sh")

  network_interface {
    network = "default"
  }

  disk {
    source_image = data.google_compute_image.hackyeah_vm_image.name
  }

  service_account {
    email  = "747661399034-compute@developer.gserviceaccount.com"
    scopes = ["cloud-platform"]
  }
}

resource "google_compute_instance_from_template" "dev-vm" {
  name = "dev-vm"
  zone = var.zone
  project = var.project_id

  source_instance_template = google_compute_instance_template.instance_template.id

  network_interface {
    network = "default"
    access_config {
      nat_ip = var.dev_ip_address
    }
  }
}