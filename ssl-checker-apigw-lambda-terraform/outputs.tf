# Output value definitions

output "apigwy_url" {
  description = "SSL Checker URL for API Gateway"

  value = aws_apigatewayv2_api.lambda.api_endpoint
}
