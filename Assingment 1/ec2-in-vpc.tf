//configuring provider
provider "aws" {
  region = "ap-southeast-1"
}
//creating vpc
resource "aws_vpc" "my_aws_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "My VPC"
  }
}
//creating public subnet
resource "aws_subnet" "my_public_subnet" {
  vpc_id     = aws_vpc.my_aws_vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "My Public Subnet"
  }
}
//creating public subnet
resource "aws_subnet" "my_private_subnet" {
  vpc_id     = aws_vpc.my_aws_vpc.id
  cidr_block = "10.0.2.0/24"

  tags = {
    Name = "My Private Subnet"
  }
}
//creating internet gateway
resource "aws_internet_gateway" "my_vpc_igw" {
  vpc_id = aws_vpc.my_aws_vpc.id

  tags = {
    Name = "My VPC IGW"
  }
}

//creating route table for public subnet
resource "aws_route_table" "public_subnet_rt" {
  vpc_id = aws_vpc.my_aws_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.my_vpc_igw.id
  }

  route {
    ipv6_cidr_block = "::/0"
    gateway_id      = aws_internet_gateway.my_vpc_igw.id
  }

  tags = {
    Name = "Public subnet route table"
  }
}

//route table association
resource "aws_route_table_association" "public_rt_ass" {
  subnet_id      = aws_subnet.my_public_subnet.id
  route_table_id = aws_route_table.public_subnet_rt.id
}


// creating security group
resource "aws_security_group" "my_vpc_sg" {
  name   = "my_vpc_sg"
  vpc_id = aws_vpc.my_aws_vpc.id


  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
  tags = {
    Name = "My Security group"
  }
}

//creating EC2 instance
resource "aws_instance" "test-instance" {
  ami = "ami-0df7a207adb9748c7"
  key_name = "test-key-pair"
  instance_type = "t2.micro"
  root_block_device {
    volume_type  = "gp2"
    volume_size  = 8
    delete_on_termination = true
  }
  tags = {
    Name = "assingment-instance"
    purpose = "Assignment"
  }
}
