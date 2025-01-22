import aws_cdk as core
import aws_cdk.assertions as assertions

from streamlit_fargate.streamlit_fargate_stack import StreamlitFargateStack

# example tests. To run these tests, uncomment this file along with the example
# resource in streamlit_fargate/streamlit_fargate_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StreamlitFargateStack(app, "streamlit-fargate")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
