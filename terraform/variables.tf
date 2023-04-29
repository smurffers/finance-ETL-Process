variable "project" {
  type = map(any)
  default = {
    id     = "fin-stocks"
    name   = "fin-stocks"
    number = 497740669112
    region = "us-east1"
    zone   = "us-east1-a"
  }
}

variable "credentials_path" {
  type    = string
  default = "C:\\Users\\1998r\\Desktop\\Projects\\ETL-Finance-Process\\keys\\fin-stocks-a52a39222581.json"
}