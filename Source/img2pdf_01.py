import img2pdf

# opening from filename
with open("name.pdf","wb") as f:
	f.write(img2pdf.convert('name.jpg'))
