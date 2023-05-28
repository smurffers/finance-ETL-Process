terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }

  backend "local" {}
}

provider "google" {
  credentials = var.credentials_path

  project = var.project["id"]
  region  = var.project["region"]
  zone    = var.project["zone"]
}

resource "google_storage_bucket" "stock-company-bucket" {
    name = "stock-companies-id"
    location = var.project["region"]
    force_destroy = true

    autoclass {
      enabled = true
    }

    versioning {
      enabled = true
    }
}