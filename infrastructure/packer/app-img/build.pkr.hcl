build {
  sources = ["sources.googlecompute.hackyeah-vm-image"]

  provisioner "file" {
    source      = "${path.root}/../../../source/hackyeah_ml"
    destination = "/apps"
  }
}