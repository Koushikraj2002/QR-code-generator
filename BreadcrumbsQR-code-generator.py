import qrcode

upi_id = input("Enter your UPI ID = ")
# codingwise@axl

#upipn://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=currency&tn=MESSAGE

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


#qr code making
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
googlepay_qr=qrcode.make(googlepay_url)
# image save pillow
paytm_qr.save('paytm_qr.png')
phonepe_qr.save('phonepe_qr.png')
googlepay_qr.save('googlepay_qr.png')

#display qr code pilow
paytm_qr.show()
phonepe_qr.show()
googlepay_qr.show()