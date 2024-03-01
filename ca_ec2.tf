resource "tls_private_key" "RSA" {

    algorithm = "RSA"
    rsa_bits = 4096  

}

resource "aws_key_pair" "CAV_keypair" {

  key_name = "CA-EC2-key"
  public_key = tls_private_key.RSA.public_key_openssh

}

resource "local_file" "CAVkeypair" {
    depends_on = [ tls_private_key.RSA ]
    content = tls_private_key.RSA.private_key_pem
    filename = "${path.module}/CAV_keypair.pem"
    file_permission = "0400"
  
}


resource "aws_instance" "test_instance" {

    ami = var.ami 
    instance_type = var.instance_type
    key_name = "${aws_key_pair.CAV_keypair.key_name}"
    security_groups = [aws_security_group.CA_SG.name]
    tags = {
            Name = var.name_tag,
            }
  
}

resource "aws_security_group" "CA_SG" {

    name = "CA_SG"
    
    ingress {
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port = 0
        to_port = 0
        protocol = -1
        cidr_blocks = ["0.0.0.0/0"]
    }
  
}