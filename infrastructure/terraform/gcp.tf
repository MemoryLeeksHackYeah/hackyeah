terraform {
  backend "gcs" {
    bucket = "hackyeah-terraform-state-bucket"
    prefix = "terraform/state"
  }
}