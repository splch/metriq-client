from metriq import MetriqClient
from metriq.models.method import MethodCreateRequest
import os

method = MethodCreateRequest()
method.name = "Test Method Name (Client)"
method.fullName = "Test Method Full Name (Client)"
method.description = "This is the first method to be successfully uploaded with the Python client."
client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.method_add(method)
assert result is not None
