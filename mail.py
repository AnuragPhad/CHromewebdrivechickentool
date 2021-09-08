import win32com.client as client

outlook=client.Dispatch("Outlook.Application")
message=outlook.CreateItem(0)
message.Display()
message.To="Anuragsadashiv.phad@scientificgames.com"
message.Subject="Testing"
message.Body="testing"
message.Save()
message.Send()
