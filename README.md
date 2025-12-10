How to use
==========

1. Deploy application to Azure
2. in cmd.exe run:
```
curl.exe -X POST https://notiapp-g5gyb5eueeh2g0ej.italynorth-01.azurewebsites.net/api/message -H "Content-Type: application/json" -d "{\"message\":\"THIS IS MY NEW MESSAGE\"}"
```
3. The webpage should display the message
