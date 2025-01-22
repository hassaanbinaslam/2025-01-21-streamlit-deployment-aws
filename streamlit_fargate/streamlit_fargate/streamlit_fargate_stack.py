import os
from aws_cdk import (
    aws_ecs as ecs,
    aws_ec2 as ec2,
    aws_ecs_patterns as ecs_patterns,
    Stack,
    CfnOutput,
)

from constructs import Construct


class StreamlitFargateStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Current directory path
        current_directory = os.path.dirname(os.path.realpath(__file__))

        # Build Dockerfile from local folder and push to ECR
        image = ecs.ContainerImage.from_asset(
            os.path.join(current_directory, "docker_lambda")
        )

        # Create a VPC for the ECS Cluster
        vpc = ec2.Vpc(
            self, "StreamlitFargateVpc", max_azs=1  # Default is all AZs in the region
        )

        # Create an ECS Cluster
        cluster = ecs.Cluster(self, "StreamlitFargateCluster", vpc=vpc)

        # Define a Fargate Task Definition and Service
        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "StreamlitFargateService",
            cluster=cluster,
            task_image_options={
                "image": image,
                "container_port": 8501,  # Streamlit default port=8501. Should be adjusted based on Dockerfile
            },
            public_load_balancer=True,
        )

        # Output the Load Balancer URL
        CfnOutput(
            self,
            "LoadBalancerDNS",
            value=fargate_service.load_balancer.load_balancer_dns_name,
        )
