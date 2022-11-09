build {
  sources = ["sources.googlecompute.hackyeah-vm-image-base"]

  provisioner "shell" {
    execute_command = "echo 'packer' | sudo -S env {{ .Vars }} {{ .Path }}"
    script          = "${path.root}/resources/install.sh"
  }
}