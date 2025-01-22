from aws_cdk import aws_lambda as _lambda, Stack, CfnOutput
from constructs import Construct


class StreamlitLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function using a Docker image
        docker_lambda = _lambda.DockerImageFunction(
            self,
            "DockerLambdaFunction",
            code=_lambda.DockerImageCode.from_image_asset("docker_lambda"),
        )

        # Add a Function URL to the Lambda function
        function_url = docker_lambda.add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE,  # No authentication (public)
        )

        CfnOutput(
            self,
            "LambdaFunctionUrl",
            value=function_url.url,
            description="The URL of the Lambda Function",
        )
