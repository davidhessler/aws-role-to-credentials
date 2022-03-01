# AWS IAM Role to Credentials

Some legacy software requires the creation of a credentials file (usually stored at `~/.aws/credentials`).

However, if you want to use an IAM role attached to an AWS Primitive (EC2 Instance, ECS Container, etc.) instead, these software doesn't work directly.

Here is a script to automatically create the credentials file from your IAM role. 
