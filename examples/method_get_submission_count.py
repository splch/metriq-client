from metriq import MetriqClient

client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTgsInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY1NzYzODl9._4CZoykTkKv_OPSWU4jNBgFhJjFH5aVOp0LubuFVA6Y")
result = client.method_get_submission_count()
assert result is not None
