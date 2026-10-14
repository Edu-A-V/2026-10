print ("Bienvenidos. Este es la mejor discoteca de latinoamerica")
edad =int(input("Cual es tu edad"))
if edad < 18:
    print ("Si eres menor de edad, no puedes ingresar")
if edad >= 18:
    print ("Puedes pasar. Te resivimos con una cerbeza gratis")
discapacidad =input("¿Tienes discapacidad visual?")
if discapacidad == "No":
    print ("Si no tienes discapacidad visual, no puedes ingresar")
if discapacidad == "Si":
    print ("Si puedes ingresar")
