provider "aws" {
  region = "eu-west-1"
}

#data "aws_ssm_parameter" "ami_id" {
#name = "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"
#}


module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs            = ["eu-west-1a"]
  public_subnets = ["10.0.1.0/24"]


}
terraform {
  backend "s3" {
    bucket = "s3-tarek-bucket-773"
    key    = "terraform.tfstates"
  }
}



resource "aws_security_group" "my-sg" {
  vpc_id = module.vpc.vpc_id
  name   = join("_", ["sg", module.vpc.vpc_id])
  dynamic "ingress" {
    for_each = var.rules
    content {
      from_port   = ingress.value["port"]
      to_port     = ingress.value["port"]
      protocol    = ingress.value["proto"]
      cidr_blocks = ingress.value["cidr_blocks"]
    }
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Websecurity-SG"
  }
}

resource "aws_instance" "my-instance" {
  ami             = "ami-0ec23856b3bad62d3"
  subnet_id       = module.vpc.public_subnets[0]
  instance_type   = "t3.micro"
  key_name = "key-1"
  security_groups = [aws_security_group.my-sg.id]
  tags = {Name = "Library web server"}

  user_data       = file("./install.sh")
}