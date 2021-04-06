##### CREATE VPC #####

aws ec2 create-vpc --cidr-block 10.10.0.0/16

## Copy VpcId from output vpc-0fecc8cd8145c7e20
## Update --vpc-id in the commands below:

aws ec2 create-subnet --vpc-id vpc-0fecc8cd8145c7e20 --cidr-block 10.10.1.0/24

aws ec2 create-subnet --vpc-id vpc-0fecc8cd8145c7e20 --cidr-block 10.10.2.0/24

## Create an Internet Gateway

aws ec2 create-internet-gateway

## Copy InternetGatewayId from the output
## Update the internet-gateway-id and vpc-id in the command below:

aws ec2 attach-internet-gateway --vpc-id vpc-0fecc8cd8145c7e20 --internet-gateway-id igw-05f4aea43456be513

## Create a custom route table

aws ec2 create-route-table --vpc-id vpc-0fecc8cd8145c7e20

## Copy RouteTableId from the output
## Update the route-table-id and gateway-id in the command below:

aws ec2 create-route --route-table-id rtb-0905b9f93dea1af9b --destination-cidr-block 0.0.0.0/0 --gateway-id igw-05f4aea43456be513

## Check route has been created and is active

aws ec2 describe-route-tables --route-table-id rtb-0905b9f93dea1af9b

## Retrieve subnet IDs
## Update VPC ID in the command below:

aws ec2 describe-subnets --filters "Name=vpc-id,Values=vpc-0fecc8cd8145c7e20" --query 'Subnets[*].{ID:SubnetId,CIDR:CidrBlock}'

## Associate subnet with custom route table to make public
## Update subnet-id and route-table-id in the command below:

aws ec2 associate-route-table  --subnet-id subnet-024bb1483cf052daf --route-table-id rtb-0905b9f93dea1af9b

## Configure subnet to issue a public IP to EC2 instances
## Update subnet-id in the command below:

aws ec2 modify-subnet-attribute --subnet-id subnet-024bb1483cf052daf --map-public-ip-on-launch


##### LAUNCH INSTANCE INTO SUBNET FOR TESTING #####

## Create a key pair and output to MyKeyPair.pem
## Modify output path accordingly

aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > ./MyKeyPair.pem

## Linux / Mac only - modify permissions

chmod 400 MyKeyPair.pem

## Create security group with rule to allow SSH

aws ec2 create-security-group --group-name SSHAccess --description "Security group for SSH access" --vpc-id vpc-0fecc8cd8145c7e20

## Copy security group ID from output
## Update group-id in the command below:

aws ec2 authorize-security-group-ingress --group-id sg-0be23d8aeb29a7de8 --protocol tcp --port 22 --cidr 0.0.0.0/0

## Launch instance in public subnet using security group and key pair created previously:
## Obtain the AMI ID from the console, update the security-group-ids and subnet-ids

aws ec2 run-instances --image-id ami-0742b4e673072066f --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-0be23d8aeb29a7de8 --subnet-id subnet-024bb1483cf052daf

## Copy instance ID from output and use in the command below
## Check instance is in running state:

aws ec2 describe-instances --instance-id i-0eea03d20ca7cf314

## Note the public IP address
## Connect to instance using key pair and public IP

ssh -i MyKeyPair.pem ec2-user@54.91.12.67



##### CLEAN UP #####

## Run commands in the following order replacing all values as necessary
aws ec2 stop-instances --instance-ids i-0eea03d20ca7cf314
aws ec2 terminate-instances --instance-ids i-0eea03d20ca7cf314
aws ec2 delete-security-group --group-id sg-0be23d8aeb29a7de8
aws ec2 delete-subnet --subnet-id subnet-024bb1483cf052daf
aws ec2 delete-subnet --subnet-id subnet-0ecc21dbfa9ea35da
aws ec2 delete-route-table --route-table-id rtb-0905b9f93dea1af9b
aws ec2 detach-internet-gateway --internet-gateway-id sg-0be23d8aeb29a7de8 --vpc-id vpc-0fecc8cd8145c7e20
aws ec2 delete-internet-gateway --internet-gateway-id sg-0be23d8aeb29a7de8
aws ec2 delete-vpc --vpc-id vpc-0fecc8cd8145c7e20
