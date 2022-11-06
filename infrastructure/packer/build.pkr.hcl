build {
  sources = ["sources.googlecompute.hackyeah-vm-image"]

  provisioner "shell" {
    execute_command = "echo 'packer' | sudo -S env {{ .Vars }} {{ .Path }}"
    script          = "${path.root}/resources/install.sh"
  }

  provisioner "file" {
    source      = "${path.root}/resources/temp.txt"
    destination = "/apps/temp.txt"
  }
}