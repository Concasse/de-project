variable "credentials" {
  description = "Credentials"
  default     = "./keys/my-creds.json"
}

variable "project" {
  description = "Project Name"
  default     = "promising-haiku-422111"
}

variable "region" {
  description = "Region Name"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "promising-haiku-422111-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}