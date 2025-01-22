import aws_cdk as core
import aws_cdk.assertions as assertions

from streamlit_lambda.streamlit_lambda_stack import StreamlitLambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in streamlit_lambda/streamlit_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StreamlitLambdaStack(app, "streamlit-lambda")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
