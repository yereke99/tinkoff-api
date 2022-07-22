data = {
	"TerminalKey": "1637858682527DEMO",
    "Password": "zch86szfax3s7hml",
	"CustomerKey": "800703982"
}

sorted_dict = dict(sorted(data.items(), key=lambda x: x[0].lower()))

for k, v in sorted_dict.items():
    print('{}: {}'.format(k, v))
