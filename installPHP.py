{
  "schemaVersion": "2.2",
  "description": "Install Dashboard App",
  "mainSteps": [
    {
      "inputs": {
        "runCommand": [
          " #!/bin/sh",
          " # Install Apache Web Server and PHP",
          " yum install -y httpd",
          " amazon-linux-extras install -y php7.2",
          " # Turn on web server",
          " systemctl enable httpd.service",
          " systemctl start  httpd.service",
          " # Download and install the AWS SDK for PHP",
          " wget https://github.com/aws/aws-sdk-php/releases/download/3.62.3/aws.zip",
          " unzip aws -d /var/www/html",
          " # Download Application files",
          " wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/169-lab-%5BJAWS%5D-systems-manager/scripts/widget-app.zip",
          " unzip widget-app.zip -d /var/www/html/"
        ]
      },
      "name": "InstallDashboardApp",
      "action": "aws:runShellScript"
    }
  ]
}