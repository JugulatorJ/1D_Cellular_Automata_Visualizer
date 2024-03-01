variable "ami" {
   type        = string
   description = "Ubuntu AMI ID in EU Central 1"
   default     = "ami-0a23a9827c6dab833"
}

variable "instance_type" {
   type        = string
   description = "Instance type"
   default     = "t2.micro"
}

variable "name_tag" {
   type        = string
   description = "Name of the EC2 instance"
   default     = "1D-Cellular Automata TEST instance"
}