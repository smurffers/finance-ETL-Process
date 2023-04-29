terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  credentials = var.credentials_path

  project = var.project["id"]
  region  = var.project["region"]
  zone    = var.project["zone"]
}

resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}
