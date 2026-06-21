terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.8.0"
    }
  }
}

provider "google" {
  project = "de-zmcamp"
  region  = "europe-west2"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "de-zmcamp-terra-bucket"
  location      = "EUROPE-WEST2"
  force_destroy = true

  uniform_bucket_level_access = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}